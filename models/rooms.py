# -*- coding: utf-8 -*-

from odoo import models, fields

class rooms(models.Model):
    _name = "hotel.rooms"
    _description = "room details for a hotel"

    company_id = fields.Many2one("res.company", store=True, copy=False,
                                string="Company",
                                default=lambda self: self.env.user.company_id.id)

    currency_id = fields.Many2one("res.currency", string="Currency",
                                related="company_id.currency_id",
                                default=lambda
                                self: self.env.user.company_id.currency_id.id)
    name = fields.Char("Room name/number", required=True, search="_search_name")
    room_image = fields.Image(string="Picture")
    selling_price = fields.Monetary("Sale price per unit", default="0.0", required=True)
    cost = fields.Monetary("Cost price per unit", default="0.0", required=True)
    hotel = fields.Many2one(string="Hotel", comodel_name="hotel.hotel", required=True)
    reservations = fields.One2many(comodel_name="hotel.reservation", inverse_name="room")

    def _search_name(self,operator,value):
        return[("Res_name",operator,value)]

    