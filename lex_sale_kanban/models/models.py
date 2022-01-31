# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LexSaleStage(models.Model):
    _name = "lex.sale.stage"

    name = fields.Char(string="Name")
    is_default = fields.Boolean(string="Default Stage", default=False)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_default_stage(self):
        stages = self.env['lex.sale.stage'].search([('is_default', '=', True)])
        if stages:
            return stages[0].id

    lex_stage_id = fields.Many2one('lex.sale.stage', string="Stage", default=_get_default_stage)