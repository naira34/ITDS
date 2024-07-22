# -*- coding: utf-8 -*-
{
    'name': 'ITDEV',
    'version': '17.0',
    'author': 'ITDS',
    'category': 'Service',
    'license': 'LGPL-3',
    'sequence': 1,
    'website': 'site',
    'description': """
    """,

    'depends': ['base', 'mail', ],
    'images' : ['static/description/icon.png', ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/client.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'test': [],

    'installable': True,
    'application': False,
    'auto_install': False,
}
