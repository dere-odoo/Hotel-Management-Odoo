# -*- coding: utf-8 -*-

from odoo import models, fields

class service(models.Model):
    _name = "hotel.service"
    _description = "Services available in hotel"
    _check_company_auto = True

    cost = fields.Float(string="Cost per unit", required=True)
    name = fields.Char(string="Name", default="cleaning service", required=True, search="_search_name")
    hotel = fields.Many2many(string="Hotel", comodel_name="hotel.hotel")

 
