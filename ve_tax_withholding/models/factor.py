# -*- coding: utf-8 -*- 

from odoo import models, fields, api 
#factor para calcular la retencion ISLR
class factor(models.Model): 
    _name = 'res.config.settings'
    _inherit = 'res.config.settings'
    
    factor = fields.Float(
    string = 'Factor Fiscal', store=True  )