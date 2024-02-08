# -*- coding: utf-8 -*-

from odoo import models, fields

class contact(models.Model):
    _name = "hotel.contact"
    _description = "contact details of customers"

    name = fields.Char(string="Name", default="contact name", required=True, search='_search_name')
    phone = fields.Char(string="Phone Number", default="0000", required=True)
    mail = fields.Char(string="Email", default="test@mail.com")
    aadhar = fields.Char(string="Aadhar card number", required=True)
    contactType = fields.Selection(string="Type of contact", selection=[("1","Customer"),("2","Employee"),("3","Manager")])
    hotels = fields.One2many(comodel_name="hotel.hotel", inverse_name="managed_by")
    reservation = fields.One2many(comodel_name="hotel.reservation", inverse_name="customer_name")
    
    def _search_name(self,operator,value):
        return[("Res_name",operator,value)]
