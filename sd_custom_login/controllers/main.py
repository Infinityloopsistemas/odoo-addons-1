﻿# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Sistemas de Datos (<http://www.sdatos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import jinja2
import os
import simplejson
import sys
import openerp
import openerp.modules.registry
from openerp.tools import topological_sort
from openerp import http
from openerp.http import request, serialize_exception as _serialize_exception

# def ensure_db(redirect='/web/database/selector'):
#     # This helper should be used in web client auth="none" routes
#     # if those routes needs a db to work with.
#     # If the heuristics does not find any database, then the users will be
#     # redirected to db selector or any url specified by `redirect` argument.
#     # If the db is taken out of a query parameter, it will be checked against
#     # `http.db_filter()` in order to ensure it's legit and thus avoid db
#     # forgering that could lead to xss attacks.
#     db = request.params.get('db')
# 
#     # Ensure db is legit
#     if db and db not in http.db_filter([db]):
#         db = None
# 
#     if db and not request.session.db:
#         # User asked a specific database on a new session.
#         # That mean the nodb router has been used to find the route
#         # Depending on installed module in the database, the rendering of the page
#         # may depend on data injected by the database route dispatcher.
#         # Thus, we redirect the user to the same page but with the session cookie set.
#         # This will force using the database route dispatcher...
#         r = request.httprequest
#         url_redirect = r.base_url
#         if r.query_string:
#             # Can't use werkzeug.wrappers.BaseRequest.url with encoded hashes:
#             # https://github.com/amigrave/werkzeug/commit/b4a62433f2f7678c234cdcac6247a869f90a7eb7
#             url_redirect += '?' + r.query_string
#         response = werkzeug.utils.redirect(url_redirect, 302)
#         request.session.db = db
#         abort_and_redirect(url_redirect)
# 
#     # if db not provided, use the session one
#     if not db and request.session.db and http.db_filter([request.session.db]):
#         db = request.session.db
# 
#     # if no database provided and no database in session, use monodb
#     if not db:
#         db = db_monodb(request.httprequest)
# 
#     # if no db can be found til here, send to the database selector
#     # the database selector will redirect to database manager if needed
#     if not db:
#         werkzeug.exceptions.abort(werkzeug.utils.redirect(redirect, 303))
# 
#     # always switch the session to the computed db
#     if db != request.session.db:
#         request.session.logout()
#         abort_and_redirect(request.httprequest.url)
# 
#     request.session.db = db

class Database_restrict(openerp.addons.web.controllers.main.Database):
        
    @http.route('/web/database/selector', type='http', auth="none")
    def selector(super, **kw):
        return http.redirect_with_hash('http://www.sdatos.com')
        #raise Exception('Not allowed')
    
    @http.route('/web/database/manager', type='http', auth="none")
    def manager(super, **kw):
        return http.redirect_with_hash('http://www.sdatos.com')
        #raise Exception('Not allowed')
    
    @http.route('/web/database/get_list', type='json', auth="none")
    def get_list(self):
        raise Exception('Not allowed')
    
    @http.route('/web/database/create', type='json', auth="none")
    def create(self, fields):
        #raise Exception('Not allowed')
        dblist = db_list(req)
        if len(dblist) > 0:
            raise Exception('Not allowed')

        return super(Database_restrict, self).create(req, fields)

    @http.route('/web/database/duplicate', type='json', auth="none")
    def duplicate(self, fields):
        raise Exception('Not allowed')
    
    @http.route('/web/database/drop', type='json', auth="none")
    def drop(self, fields):
        raise Exception('Not allowed')
    
    @http.route('/web/database/backup', type='http', auth="none")
    def backup(self, backup_db, backup_pwd, token, backup_format='zip'):
        raise Exception('Not allowed')
    
    @http.route('/web/database/restore', type='http', auth="none")
    def restore(self, db_file, restore_pwd, new_db, mode):
        raise Exception('Not allowed')
    @http.route('/web/database/change_password', type='json', auth="none")
    def change_password(self, fields):
        raise Exception('Not allowed')
    
Database_restrict()

# cont = 4
# 
# class Home_error_pass(openerp.addons.web.controllers.main.Home):
# 
#     @http.route('/web/login', type='http', auth="none")
#     def web_login(self, redirect=None, **kw):
#         ensure_db()
# 
#         if request.httprequest.method == 'GET' and redirect and request.session.uid:
#             return http.redirect_with_hash(redirect)
# 
#         if not request.uid:
#             request.uid = openerp.SUPERUSER_ID
# 
#         values = request.params.copy()
#         if not redirect:
#             redirect = '/web?' + request.httprequest.query_string
#         values['redirect'] = redirect
# 
#         try:
#             values['databases'] = http.db_list()
#         except openerp.exceptions.AccessDenied:
#             values['databases'] = None
# 
#         if request.httprequest.method == 'POST':
#             old_uid = request.uid
#             uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
#             if uid is not False:
#                 return http.redirect_with_hash(redirect)
#             request.uid = old_uid
#             global cont
#             cont = cont - 1
#             values['error'] = "Error user/pass, le quedan %s intentos antes de que se bloquee el usuario" %str(cont)
#             if cont <= 0:
#                cont = 4
#                raise Exception('Pass error')
#         return request.render('web.login', values)
#         
# Home_error_pass()