from odoo import models, fields

class contact(models.Model):
    _name = "contact"
    _description = "contact details of customers"

    name = fields.Char('Name', default='contact name', required=True)
    phone = fields.Char('Phone Number',default='0000' ,required=True)
    mail = fields.Char('Email',default='test@mail.com')
    aadhar = fields.Char("Aadhar card number",required=True)
    contactType = fields.Selection([('1',"Customer"),('2',"Employee"),('3',"Manager")])
    # relatedHotel = fields.Many2one()