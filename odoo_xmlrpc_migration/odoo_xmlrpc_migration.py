# -*- coding: utf-8 -*-

import xmlrpc.client as xmlrpclib
from configparser import ConfigParser
import ssl
import sys

# Class OdooXmlrpcMigration


class OdooXmlrpcMigration(object):
    socks = {}

    system_fields = ['id', 'write_date', 'write_uid',
                     'create_date', 'create_uid', '__last_update']

    # Constructor

    def __init__(self, config_file='./odoo_xmlrpc_migration.conf'):
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

    def fields_get(self, server, model):
        server = self.socks[server]
        sock = server['sock']
        domain = [(1, '=', 1)]
        ids = sock.execute(
            server['dbname'],
            server['uid'],
            server['passwd'],
            model,
            'search',
            domain,
            []
        )
        records = []
        for id in ids:
            rec = sock.execute(
                server['dbname'],
                server['uid'],
                server['passwd'],
                model,
                'read',
                [id]
                )
            records.append(rec)
        return records
