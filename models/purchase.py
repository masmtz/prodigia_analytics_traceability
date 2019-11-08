# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        for rec in res:
            rec['analytic_account_id'] = self.account_analytic_id.id
            rec['analytic_account_tag_ids'] = [[6, 0, self.analytic_tag_ids.ids]]

        return res
