# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class LexSaleStage(models.Model):
    _name = "lex.sale.stage"
    _fold_name = "fold"

    name = fields.Char(string="Name")
    is_default = fields.Boolean(string="Default Stage", default=False)
    fold = fields.Boolean(string="Folded in Kanban", help="This stage is folded in the Kanban view.")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_default_stage(self):
        stages = self.env['lex.sale.stage'].search([('is_default', '=', True)])
        if stages:
            return stages[0].id

    lex_stage_id = fields.Many2one('lex.sale.stage', string="Stage", group_expand='_expand_stages', default=_get_default_stage)
    lex_is_closed = fields.Boolean(string="Closed", compute="_compute_check_fold_state", store=False)
    
    def _expand_stages(self, states, domain, order):
        stage_ids = self.env['lex.sale.stage'].search([])
        return stage_ids
    
    def _compute_check_fold_state(self):
        if self.lex_stage_id and self.lex_stage_id.fold:
            self.lex_is_closed = True
        else:
            self.lex_is_closed = False
    
    def set_as_complete(self):
        stage_id = self._get_complete_stage()
        
        if not stage_id:
            raise UserError('Please create a new Fold Stage in the Kanban view.')
        
        self.lex_stage_id = stage_id
        
    def _get_complete_stage(self):
        stages = self.env['lex.sale.stage'].search([('fold', '=', True)])
        if stages:
            return stages[0].id
        return False