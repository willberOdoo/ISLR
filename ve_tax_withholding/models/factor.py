# -*- coding: utf-8 -*- 

from odoo import models, fields, api 
#factor para calcular la retencion ISLR
class factor(models.TransientModel): 
    
    _inherits = 'res.config.settings'
    
    factor = fields.Float(
    string = 'Factor Fiscal', store=True,  )