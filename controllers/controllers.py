# -*- coding: utf-8 -*-
# from odoo import http


# class QuanLyNhaTro(http.Controller):
#     @http.route('/quan_ly_nha_tro/quan_ly_nha_tro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quan_ly_nha_tro/quan_ly_nha_tro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quan_ly_nha_tro.listing', {
#             'root': '/quan_ly_nha_tro/quan_ly_nha_tro',
#             'objects': http.request.env['quan_ly_nha_tro.quan_ly_nha_tro'].search([]),
#         })

#     @http.route('/quan_ly_nha_tro/quan_ly_nha_tro/objects/<model("quan_ly_nha_tro.quan_ly_nha_tro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quan_ly_nha_tro.object', {
#             'object': obj
#         })

