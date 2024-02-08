# -*- coding: utf-8 -*-

from odoo import models, fields

class hotel(models.Model):
    _name = "hotel.hotel"
    _description = "Hotel specific information"

    name = fields.Char(string="Name", default="Hotel Name", required=True, search="_search_name")
    hotel_image = fields.Image(string="Picture")
    address = fields.Text(string="Hotel Address", default="address")
    managed_by = fields.Many2one(string="Manager", comodel_name="hotel.contact", required=True)
    reservations = fields.One2many(comodel_name="hotel.reservation", inverse_name="hotel")
    rooms = fields.One2many(comodel_name="hotel.rooms", inverse_name="hotel")
    services = fields.One2many(comodel_name="hotel.service", inverse_name="hotel")

    def _search_name(self,operator,value):
        return[("Res_name",operator,value)]
