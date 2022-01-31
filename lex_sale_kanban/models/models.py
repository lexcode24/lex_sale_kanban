# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LexSaleStage(models.Model):
    _name = "lex.sale.stage"

    name = fields.Char(string="Name")
    is_default = fields.Boolean(string="Default Stage")