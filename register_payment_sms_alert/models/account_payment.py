# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
import requests

class account_payment(models.Model):
    
    _inherit = 'account.payment'
    
    @api.multi
    def write(self, values):
        
        # only a draft invoice can be posted
        for partner in self.partner_id:
            if self.state == 'draft' and 'move_name' in values:
                #partner_ids = self.env['res.partner'].browse(self.partner_id)
                username = self.env['ir.config_parameter'].get_param('novaji_bulk_sms_username')
                password = self.env['ir.config_parameter'].get_param('novaji_bulk_sms_password')
                sender = self.env['ir.config_parameter'].get_param('novaji_bulk_sms_sender')
                template = self.env['ir.config_parameter'].get_param('novaji_bulk_sms_message')
                message = template.format(amount="{:,.2f}".format(self.amount), name=partner.name)
                destination = str(partner.phone)
                if type(destination) == str and len(destination) <= 10:
                    destination = str(self.partner.mobile)           
                endpoint = "http://sms.novajii.com/sms/api/send?username={uname}&password={pwd}&sender={sender}&destination={dst}&message={msg}".format(uname=username, pwd=password, sender=sender, dst=destination, msg=message)
                if self.payment_type == 'inbound' and len(destination) >= 10:
                    try:
                        r = requests.get(endpoint)
                    except:
                           pass
                    #raise Warning(r.text)
                    #return {'value':{},'warning':{'title':'Warning','message':r.text}}
                 
                #except:
                #pass
                            
        #print(r.text)                          
        
        return super(account_payment, self).write(values)