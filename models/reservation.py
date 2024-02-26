# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError


class reservation(models.Model):
    _name = "hotel.reservation"
    _description = "all customer reservation"
    _check_company_auto = True

    res_name = fields.Char(string="Name", required=True)
    selling_price = fields.Float(string="Expected price", required=True, compute="_compute_selling_price")
    discounted_price = fields.Float(string="Discounted Price", compute="_compute_discounted_price")
    stay_for = fields.Integer(string="Number of days", required=True)
    hotel_id = fields.Many2one(string="Hotel", comodel_name="hotel.hotel", required=True)
    hotel_address = fields.Text(related="hotel_id.address")
    reservation_line_ids = fields.One2many(string="room", comodel_name="hotel.reservation.line", inverse_name="reservation_id")
    start_date = fields.Date()
    end_date = fields.Date(string="End Date", compute="_compute_end_date", store=True, readonly=True)
    customer = fields.Many2one(string="Customer", comodel_name="res.users", required=True)
    active = fields.Boolean(string="Active", default=True)
    comments = fields.Text(string="Comments")

    @api.depends("start_date", "stay_for")
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.stay_for:
                record.end_date = record.start_date+timedelta(days=record.stay_for)

    @api.depends("reservation_line_ids")
    def _compute_selling_price(self):
        total = 0
        offers = self.reservation_line_ids
        for record in offers:
            total += record.room_id.selling_price
        self.selling_price = total*self.stay_for

    def _compute_discounted_price(self):
        total = 0
        offers = self.reservation_line_ids
        for record in offers:
            total += record.room_price
        self.discounted_price = total*self.stay_for

    
    