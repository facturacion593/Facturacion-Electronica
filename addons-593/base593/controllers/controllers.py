# -*- coding: utf-8 -*-
from odoo import http

# class Base593(http.Controller):
#     @http.route('/base593/base593/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base593/base593/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base593.listing', {
#             'root': '/base593/base593',
#             'objects': http.request.env['base593.base593'].search([]),
#         })

#     @http.route('/base593/base593/objects/<model("base593.base593"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base593.object', {
#             'object': obj
#         })