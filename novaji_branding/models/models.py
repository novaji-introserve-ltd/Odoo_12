# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class novaji_branding(models.Model):
#     _name = 'novaji_branding.novaji_branding'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class res_company(models.Model):

    _inherit = 'res.company'

    #num_employees = fields.Integer('Staff Strength',help="Company Staff Count")
    #app_title = fields.Char('App Title')
