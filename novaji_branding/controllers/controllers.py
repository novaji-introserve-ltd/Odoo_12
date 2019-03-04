# -*- coding: utf-8 -*-
from openerp import http

# class NovajiBranding(http.Controller):
#     @http.route('/novaji_branding/novaji_branding/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/novaji_branding/novaji_branding/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('novaji_branding.listing', {
#             'root': '/novaji_branding/novaji_branding',
#             'objects': http.request.env['novaji_branding.novaji_branding'].search([]),
#         })

#     @http.route('/novaji_branding/novaji_branding/objects/<model("novaji_branding.novaji_branding"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('novaji_branding.object', {
#             'object': obj
#         })