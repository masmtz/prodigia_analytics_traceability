# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _prepare_invoice_line_from_po_line(self, line):
        values = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(line)

        values.update({
                'account_analytic_id': line.account_analytic_id.id,
                'analytic_tag_ids': line.analytic_tag_ids.ids
            })

        return values
