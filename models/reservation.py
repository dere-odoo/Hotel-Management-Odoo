# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError, UserError


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
    start_date = fields.Date(required = True)
    end_date = fields.Date(string="End Date", compute="_compute_end_date", store=True, readonly=True)
    customer_id = fields.Many2one(string="Customer", comodel_name="res.users", required=True)
    active = fields.Boolean(string="Active", default=True)
    comments = fields.Text(string="Comments")
    state = fields.Selection(string="state", default="draft",
        selection=[("draft", "Draft"), ("booked", "Booked"), ("canceled", "Canceled")]
    )

    _sql_constraints = [
        ("check_stay_for_positive", "CHECK (stay_for > 0)", "Number of days must be strictly positive")
    ]

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


    def action_reservation_book(self):
        self.ensure_one()
        breakpoint()
        cur_rooms = [reservation_line.room_id.id for reservation_line in self.reservation_line_ids] 
        reservations_count = self.search_count([("hotel_id", "=", self.hotel_id.id), ("end_date", ">=" , fields.Date.to_date(self.start_date)), ("state", "=", "booked"), ("reservation_line_ids.room_id.id", "in", cur_rooms)])
        if reservations_count > 0:
            raise UserError("One of the rooms in this reservations is already booked")
        self.state = "booked"
    
    def action_reservation_cancel(self):
        self.ensure_one()
        self.state = "canceled"