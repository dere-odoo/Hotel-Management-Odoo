# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = "hotel.hotel"
    _description = "Hotel specific information"

    name = fields.Char(string="Name", required=True, search="_search_name")
    hotel_image = fields.Image(string="Picture")
    address = fields.Text(string="Hotel Address", required=True)
    managed_by = fields.Many2one(string="Manager", comodel_name="res.users", required=True, domain=lambda self: [('groups_id', 'in', [self.env.ref('Hotel-Management-Odoo.group_manager').id])])
    room_ids = fields.One2many(string="Rooms", comodel_name="hotel.rooms", inverse_name="hotel_id")
    service_ids = fields.Many2many(string="Available Services", comodel_name="hotel.service")
    reservation_ids = fields.One2many(string="Reservations", comodel_name="hotel.reservation", inverse_name="hotel_id")
    reservation_count = fields.Integer(string="Reservations")
    description = fields.Text(string="Description", default="Some hotel description")

    @api.depends("reservation_ids")
    def _compute_reservation_count(self):
        self.reservation_count = len(self.reservation_ids)
