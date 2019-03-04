# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class PayAsYouEarn(models.Model):
    _inherit = 'hr.payslip'

    @api.multi
    def calculate_paye(self,wage,basic,transportation,housing):
        taxable = 0
        #wage = 150000
        #basic = 22500
        #transportation = 22500
        #housing = 52500
        monthly = wage * 0.9
        #monthly = contract.wage
        annual = monthly * 12
        relief = (annual * 0.2) + 200000
        #pension = annual * 0.08
        pension = (basic + transportation + housing)  * 0.08 * 12 
        #nhf = annual * 0.025
        nhf = (basic * 0.025) * 12 
        exemption = pension + nhf + relief
        if (annual <= exemption):
            exemption = annual
        else:
            taxable = annual - exemption
        # 7% for the first 300,000
        p1  = (min(taxable, 300000) * 0.07) if taxable <= 300000 else (300000 * 0.07)
        # 11% on the next amount above 300,000 but less than 600,000
        p2  = (min(300000, taxable-300000) * 0.11) if (taxable > 300000 and taxable <= 600000) else 0
        # 15% on the next amount above 600,000
        p3  = (min(500000, taxable-600000) * 0.15) if (taxable > 600000 and taxable <= 1100000) else 0
        # 19% on next amount above 1,100,000 to a cap of 1,600,000
        p4  = (min(500000, taxable-1100000) * 0.19) if (taxable > 1100000 and taxable <= 1600000) else 0
        #21% on next amount above 1,600,000 to a cap of 3,200,000
        p5  = (min(1600000, taxable-1600000) * 0.21) if (taxable > 1600000 and taxable <= 3200000) else 0
        #24% on anything  3,200,000 and above
        p6  = ((taxable-3200000) * 0.24) if taxable > 3200000 else 0
        tax = p1 + p2 + p3 + p4 + p5 + p6
        result = (tax / 12) * (-1)
        return result

