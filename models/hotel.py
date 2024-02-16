# -*- coding: utf-8 -*-

from odoo import models, fields

class hotel(models.Model):
    _name = "hotel.hotel"
    _description = "Hotel specific information"

    name = fields.Char(string="Name", required=True, search="_search_name")
    hotel_image = fields.Image(string="Picture")
    address = fields.Text(string="Hotel Address", required=True)
    managed_by = fields.Many2one(string="Manager", comodel_name="res.users", required=True)
    room_ids = fields.One2many(string="Rooms", comodel_name="hotel.rooms", inverse_name="hotel_id")
