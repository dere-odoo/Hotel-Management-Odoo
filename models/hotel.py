# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = "hotel.hotel"
    _description = "Hotel specific information"

    name = fields.Char(string="Name", required=True, search="_search_name")
    hotel_image = fields.Image(string="Picture", attachment=True)
    address = fields.Text(string="Hotel Address", required=True)
    managed_by = fields.Many2one(string="Manager", comodel_name="res.users", required=True, domain=lambda self: [('groups_id', 'in', [self.env.ref('Hotel-Management-Odoo.group_manager').id])])
    room_ids = fields.One2many(string="Rooms", comodel_name="hotel.rooms", inverse_name="hotel_id")
    service_ids = fields.Many2many(string="Available Services", comodel_name="hotel.service")
    reservation_ids = fields.One2many(string="Reservations", comodel_name="hotel.reservation", inverse_name="hotel_id")
    description = fields.Text(string="Description", default="Some hotel description")
    contact_info_mail = fields.Char(string="Contact Email")
    contact_info_phone = fields.Char(string="Contact Phone")
    number_of_rooms = fields.Integer(string="Rooms", compute="_compute_number_of_rooms", store=True)
    number_of_reservations = fields.Integer(string="Reservations", compute="_compute_number_of_reservation", store=True)

    @api.depends("reservation_ids")
    def _compute_number_of_reservation(self):
        for record in self:
            record.number_of_reservations = len(record.reservation_ids)

    @api.depends("room_ids")
    def _compute_number_of_rooms(self):
        self.number_of_rooms = len(self.room_ids)

