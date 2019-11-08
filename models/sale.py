# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Cuenta analitica')


    @api.multi
    def _prepare_procurement_values(self, group_id=False):
        """ Prepare specific key for moves or other components that will be created from a procurement rule
        comming from a sale order line. This method could be override in order to add other custom key that could
        be used in move/po creation.
        """
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        for rec in self:
            values.update({
                'analytic_account_id': rec.analytic_account_id.id,
                'analytic_account_tag_ids': [[6, 0, rec.analytic_tag_ids.ids]],
            })
        return values


    @api.multi
    def _prepare_invoice_line(self, qty):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.
        """
        values = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        values.update({
            'account_analytic_id': self.analytic_account_id.id,
            'analytic_tag_ids': [[6, 0, self.analytic_tag_ids.ids]],
        })
        return values
