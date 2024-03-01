# -*- coding: utf-8 -*-

from odoo import models, api, fields

class reservation_line(models.Model):
    _name="hotel.reservation.line"
    _description="Connection between room,reservation and final price for each room"

    reservation_id = fields.Many2one(comodel_name="hotel.reservation")
    hotel_id = fields.Many2one(related="reservation_id.hotel_id", required=True)
    room_price = fields.Float(string="Price", compute="_fetch_price", store=True, readonly=False)
    allowed_room_id = fields.One2many(related="hotel_id.room_ids")
    room_id = fields.Many2one(comodel_name="hotel.rooms", required=True)
    start_date = fields.Date(related="reservation_id.start_date", store=True)
    end_date = fields.Date(related="reservation_id.end_date", store=True)

    _sql_constraints = [
        ("check_price_positive", "room_price > 0", "Room Price must be strictly positive")
    ]

    @api.depends("room_id")
    def _fetch_price(self):
        for record in self:
            if record.room_id:
                record.room_price = record.room_id.selling_price
            else:
                record.room_price = 0.0
    