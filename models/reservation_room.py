# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reservation_room(models.Model):
    _name="hotel.reservation_room_price"
    _description="Connection between room,reservation and final price for each room"

    reservation_id = fields.Many2one(comodel_name="hotel.reservation")
    hotel_id = fields.Many2one(related="reservation_id.hotel_id", required=True)
    room_price = fields.Float(string="Price", compute="_fetch_price", store=True, readonly=False)
    room_id = fields.Many2one(comodel_name="hotel.rooms")

    @api.onchange('hotel_id')
    def _compute_room_ids(self):
        for rec in self:
            res = {"domain":{"room_id":[("hotel_id","=",rec.hotel_id)]}}
            # breakpoint()
            return res

    @api.depends("room_id")
    def _fetch_price(self):
        for record in self:
            if record.room_id:
                record.room_price = record.room_id.selling_price
            else:
                record.room_price = 0.0
    
    
    