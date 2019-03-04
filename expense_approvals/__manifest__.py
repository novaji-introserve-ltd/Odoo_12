# -*- coding: utf-8 -*-
{
    'name': "Extra Expense Approvals",

    'summary': """
       Additional approvals levels for Expense""",

    'description': """
          Adds additional approvals levels for expense:
          - Approved by Accounts > Approved by Finance > Approved by Treasury
    """,

    'author': "NOVAJI INTROSERVE LIMITED",
    'website': "http://www.novajii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '3.0',

    # any module necessary for this one to work correctly
    'depends': ['hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
}