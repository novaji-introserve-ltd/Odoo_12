# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import _
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class HrExpenseSheet(models.Model):
    _inherit = ['hr.expense.sheet']
    state = fields.Selection([('submit', 'Submitted'),
                             ('finance', 'Finance'),
                             ('approve', 'Approved'),
                             ('post', 'Posted'),
                             ('done', 'Paid'),
                             ('cancel', 'Refused')
                             ], string='Status', index=True, readonly=True, track_visibility='onchange', copy=False, default='submit', required=True,
                             help='Expense Report State')
    
    @api.multi
    def approved_by_finance(self):
        self.write({'state': 'finance'})
        
    @api.multi
    def approved_by_treasury(self):
        #self.write({'state': 'approve'})
        self.approve_expense_sheets()
    
