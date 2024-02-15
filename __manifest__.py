# -*- coding: utf-8 -*-
{
    'name': "Owl Dashboard",
    'summary': """Best Custom Dashboard""",
    'description': """Owl Custom Dashboard""",
    'author': "Tasin Tarek",
    'website': "https://tasin-tarek.odoo.com/",
    'category': 'Customizations',
    'version': '17.1',
    'depends': [
        'base',
        'web',
        'sale',
        'board',
    ],
    'data': [
        'views/sales_dashboard_view.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'smart_dashboard/static/src/components/**/*.js',
            'smart_dashboard/static/src/components/**/*.xml',
            'smart_dashboard/static/src/components/**/*.scss',
        ],
    },
}
