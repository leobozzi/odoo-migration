# -*- coding: utf-8 -*-

import xmlrpc.client as xmlrpclib
from configparser import ConfigParser
import ssl
import sys

# Class OdooXmlrcpMigration


class OdooXmlrcpMigration(object):
    socks = {}

    # Constructor
    def __init__(self, config_file='./odoo_xmlrcp_migration.conf'):
        gcontext = ssl._create_unverified_context()
        self.config = ConfigParser()
        self.config.read(config_file)
        self.socks['from'] = {
            'dbname': self.config.get('odooserver-origin', 'dbname'),
            'username': self.config.get('odooserver-origin', 'username'),
            'passwd': self.config.get('odooserver-origin', 'passwd'),
            'url': self.config.get('odooserver-origin', 'url'),
        }
        self.socks['from']['sock_common'] = xmlrpclib.ServerProxy(
            '%s/xmlrpc/common' % (self.socks['from']['url']), context=gcontext)
        self.socks['from']['uid'] = self.socks['from']['sock_common'].login(
            self.socks['from']['dbname'],
            self.socks['from']['username'],
            self.socks['from']['passwd'])
        self.socks['from']['sock'] = xmlrpclib.ServerProxy(
            '%s/xmlrpc/object' % (self.socks['from']['url']), context=gcontext)

        self.socks['to'] = {
            'dbname': self.config.get('odooserver-destination', 'dbname'),
            'username': self.config.get('odooserver-destination', 'username'),
            'passwd': self.config.get('odooserver-destination', 'passwd'),
            'url': self.config.get('odooserver-destination', 'url'),
        }
        self.socks['to']['sock_common'] = xmlrpclib.ServerProxy(
            '%s/xmlrpc/common' % (self.socks['to']['url']), context=gcontext)
        self.socks['to']['uid'] = self.socks['to']['sock_common'].login(
            self.socks['to']['dbname'],
            self.socks['to']['username'],
            self.socks['to']['passwd'])
        self.socks['to']['sock'] = xmlrpclib.ServerProxy(
            '%s/xmlrpc/object' % (self.socks['to']['url']), context=gcontext)
