# -*- coding: utf-8 -*-
from odoo import http

# class NovajiPayroll(http.Controller):
#     @http.route('/novaji_payroll/novaji_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/novaji_payroll/novaji_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('novaji_payroll.listing', {
#             'root': '/novaji_payroll/novaji_payroll',
#             'objects': http.request.env['novaji_payroll.novaji_payroll'].search([]),
#         })

#     @http.route('/novaji_payroll/novaji_payroll/objects/<model("novaji_payroll.novaji_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('novaji_payroll.object', {
#             'object': obj
#         })