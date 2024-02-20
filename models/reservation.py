# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError


class reservation(models.Model):
    _name = "hotel.reservation"
    _description = "all customer reservation"
    _check_company_auto = True

    res_name = fields.Char(string="Name", required=True)
    selling_price = fields.Float(string="Unit price", required=True)
    stay_for = fields.Integer(string="Number of days", required=True)
    hotel_id = fields.Many2one(string="Hotel", comodel_name="hotel.hotel", required=True)
    hotel_address = fields.Text(related="hotel_id.address")
    reservation_room = fields.One2many(string="room", comodel_name="hotel.reservation.line", inverse_name="reservation_id")
    start_date = fields.Date()
    end_date = fields.Date(string="End Date", compute="_compute_end_date", store=True, readonly=True)
    customer = fields.Many2one(string="Customer", comodel_name="res.users", required=True)

    @api.depends("start_date", "stay_for")
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.stay_for:
                record.end_date = record.start_date+timedelta(days=record.stay_for)

    
    