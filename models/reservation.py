# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reservation(models.Model):
    _name = "hotel.reservation"
    _description = "all customer reservation"
    _check_company_auto = True

    company_id = fields.Many2one("res.company", store=True, copy=False,
                                string="Company",
                                default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one("res.currency", string="Currency",
                                related="company_id.currency_id",
                                default=lambda
                                self: self.env.user.company_id.currency_id.id)
    res_name = fields.Char(string="Name", search="_search_name",required=True)
    customer_name = fields.Many2one(string="Customer", comodel_name="hotel.contact")
    selling_price = fields.Monetary("Unit price", required=True)
    stayFor = fields.Date()
    hotel = fields.Many2one(string="Hotel", comodel_name="hotel.hotel", required=True)
    hotelName = fields.Char(related="hotel.name")
    room = fields.Many2one(string="Room", comodel_name="hotel.rooms", required=True )
    startDate = fields.Date(default=fields.Date.today())
    endDate = fields.Date(string="End Date", compute="_compute_ed_date", store=True, readonly=True)

    @api.depends("startDate","stayFor")
    def _compute_end_date(self):
        if record.startDate and record.stayFor:
            record.endDate = record.startDate+record.endDate
    
    def _search_name(self,operator,value):
        return[("Res_name",operator,value)]
    