# -*- coding: utf-8 -*-
{
    'name': "Payroll - Nigeria",

    'summary': """
       Additional payroll configuration by NOVAJI INTROSERVE LIMITED""",

    'description': """
          Additional payroll configuration by NOVAJI INTROSERVE LIMITED.
          This includes:
          Salary Rules: P.A.Y.E with computation
    """,

    'author': "NOVAJI INTROSERVE LIMITED",
    'website': "http://www.novajii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '2.9',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/hr_payroll_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}