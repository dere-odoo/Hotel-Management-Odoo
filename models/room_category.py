# -*- coding: utf-8 -*-

from odoo import models, fields

class RoomCategory(models.Model):
    _name = "hotel.room.category"
    _description = "Room Category"

    name = fields.Char(string="Name", required=True)