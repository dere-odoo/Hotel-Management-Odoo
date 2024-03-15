# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RoomCategory(models.Model):
    _name = "hotel.room.category"
    _description = "Room Category"

    name = fields.Char(string="Name", required=True)
    room_ids = fields.Many2many(comodel_name="hotel.rooms")
    number_of_rooms = fields.Integer(string="Rooms", compute="_compute_number_of_rooms")

    @api.depends("room_ids")
    def _compute_number_of_rooms(self):
        for record in self:
            record.number_of_rooms = len(record.room_ids)