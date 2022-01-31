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
    'category': 'Sales',
    'version': '15.0.0.1',
    'license': 'AGPL-3',
    'price': 19.95,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/inherit.xml',
    ]
}
