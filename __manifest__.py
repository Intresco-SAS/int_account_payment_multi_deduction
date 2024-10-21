# -*- coding: utf-8 -*-
{
    'name': "Payment Register with Multiple Deduction Improvmement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Intresco SAS",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'accounting',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        'account_payment_multi_deduction',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_payment_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': True,
}
