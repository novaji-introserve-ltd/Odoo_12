# -*- coding: utf-8 -*-
{
    'name': "NOBUS Install and Setup",

    'summary': """
        Installations and Setup""",

    'description': """
        Backend Customizations by Novaji Introserve
    """,

    'author': "Novaji Introserve Limited",
    'website': "http://www.novajii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_automation', 'account_cancel', 'account_payment', 'calendar', 'contacts', 'crm', 'document', 'google_drive', 'hr', 'hr_contract', 'hr_expense', 'hr_holidays', 'hr_maintenance', 'hr_org_chart', 'hr_payroll', 'lunch', 'maintenance', 'mass_mailing', 'note', 'product', 'project', 'product_expiry', 'purchase', 'purchase_requisition',
    'repair', 'sale', 'sale_margin', 'sale_expense', 'app_odoo_customize', 'novaji_payroll'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
}
