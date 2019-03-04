# -*- coding: utf-8 -*-
{
    'name': "Register Payment SMS Alert",

    'summary': """
        Send NOVAJI SMS alert to Customer when payment is registered""",

    'description': """
       Send SMS using NOVAJI API to customer when a payment is validated
    """,

    'author': "Novaji Introserve Limited",
    'website': "http://www.novajii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Web',
    'version': '12.0.6',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'data/ir_config_parameter.xml',
        'views/menuitems.xml',
        'views/views.xml',
    ],
}
