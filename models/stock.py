# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def _get_analytic(self):
        for rec in self:
            if rec.picking_type_id.code == 'outgoing':
                if rec.sale_id.analytic_account_id:
                    rec.analytic_account_id = rec.sale_id.analytic_account_id.id
            elif rec.picking_type_id.code == 'incoming':
                if rec.purchase_id.analytic_account_id:
                    rec.analytic_account_id = rec.purchase_id.analytic_account_id.id
            # elif rec.picking_type_id.code == 'internal':
                # rec.analytic_account_id = rec.analytic_id
                # rec.analytic_account_id = self.env['account.analytic.account'].search([('sucursal_id','=',self.env.user.current_sucursal_id.id)])

    account_analytic_id = fields.Many2one('account.analytic.account', string='Cuenta Analítica', compute='_get_analytic')
    analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Etiquetas Analíticas')

    # CAMPOS DE ANALITICAS PARA MOVIMIENTOS INTERNOS
    analytic_acc_id = fields.Many2one('account.analytic.account', string='Cuenta Analítica')


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    analytic_account_id = fields.Many2one(
        'account.analytic.account', string='Cuenta Analítica', ondelete='set null', required=True)
    analytic_account_tag_ids = fields.Many2many('account.analytic.tag', string='Etiquetas Analíticas')


class StockInventoryLine(models.Model):
    _inherit = 'stock.inventory.line'

    def _get_move_values(self, qty, location_id, location_dest_id, out):
        res = super(StockInventoryLine, self)._get_move_values(qty, location_id, location_dest_id, out)
        res['analytic_account_id'] = self.inventory_id.analytic_account_id.id
        res['analytic_account_tag_ids'] = [[6, 0, self.inventory_id.analytic_account_tag_ids.ids]]

        return res


class StockMove(models.Model):
    _inherit = 'stock.move'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Cuenta analitica', ondelete='set null')
    analytic_account_tag_ids = fields.Many2many('account.analytic.tag', string='Etiquetas Analíticas')

    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id):
        res = super(StockMove, self)._prepare_account_move_line(
            qty, cost, credit_account_id, debit_account_id)
        for rec in res:
            rec[2]['account_analytic_id'] = self.analytic_account_id.id or self.inventory_id.analytic_account_id.id or self.picking_id.account_analytic_id.id
            rec[2]['analytic_account_id'] = self.analytic_account_id.id or self.inventory_id.analytic_account_id.id or self.picking_id.account_analytic_id.id
            rec[2]['analytic_tag_ids'] = [[6, 0, self.analytic_account_tag_ids.ids]]

        return res

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, values, group_id):
        res = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, values, group_id)
        res['analytic_account_id'] = values.get('analytic_account_id')
        res['analytic_account_tag_ids'] = values.get('analytic_account_tag_ids')

        return res
