# -*- coding: utf-8 -*-
{
    'name': "Warranty",

    'summary': """
        The module at Artarad Company provides the necessary guarantees for the
        activities and contracts with customers in accordance with the customary
        procedures in the country.""",

    'description': """
        This system provides the user with the following features:
        - Possibility to register the guarantee by bank warranty
        - Possibility to register the guarantee by bank check
        - Possibility to register the guarantee by promissory note
    """,

    'author': "Artarad",
    'website': "http://artarad.ir/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
