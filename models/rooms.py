# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rooms(models.Model):
    _name = "hotel.rooms"
    _description = "room details for a hotel"

    name = fields.Char("Room name/number", required=True)
    room_image = fields.Image(string="Picture", store=True)
    selling_price = fields.Float(string="Sale price per unit", default="0.0", required=True)
    hotel_id = fields.Many2one(string="Hotel", comodel_name="hotel.hotel", required=True, search="_search_hotel_id")
    reservation_line_ids = fields.One2many(string="Reservations", comodel_name="hotel.reservation.line", inverse_name="room_id")
    category_ids = fields.Many2many(string="Category", comodel_name="hotel.room.category")
    number_of_reservations = fields.Integer(string="Reservations", compute="_compute_number_reservation", store=True)

    @api.depends("reservation_line_ids")
    def _compute_number_reservation(self):
        for record in self:
            record.number_of_reservations = len(record.reservation_line_ids)

    def _search_hotel_id(self, operator,value):
        return[("hotel_id",operator,value)]