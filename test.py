#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo_xmlrcp_migration.odoo_xmlrcp_migration import OdooXmlrcpMigration

import os

path = os.path.abspath(os.getcwd())
prueba = OdooXmlrcpMigration(
    config_file='%s/odoo_xmlrcp_migration.conf' % (path))
