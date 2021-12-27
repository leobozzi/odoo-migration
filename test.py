#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo_xmlrpc_migration.odoo_xmlrpc_migration import OdooXmlrpcMigration

import os

path = os.path.abspath(os.getcwd())
prueba = OdooXmlrpcMigration(
    config_file='%s/odoo_xmlrpc_migration.conf' % (path))

fields_from = prueba.fields_get('from', 'res.partner')

fields_to = prueba.fields_get('to', 'res.partner')

set_from = set(fields_from[0][0].keys())
set_to = set(fields_to[0][0].keys())

print(set_from-set_to)

#fields = prueba.fields_get('to', 'res.partner')
#print(len(fields))
