# -*- coding: utf-8 -*-
{
    'name': "Sale Kanban",

    'summary': """
        Kanban view for Sale module""",

    'description': """
    """,

    'author': "Alexander Kroeker",
    'website': "https://www.lexcode.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
