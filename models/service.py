# -*- coding: utf-8 -*-

from odoo import models, fields, api

class service(models.Model):
    _name = "hotel.service"
    _description = "Services available in hotel"
    _check_company_auto = True

    cost = fields.Float(string="Cost per unit", required=True)
    name = fields.Char(string="Name", default="cleaning service", required=True, search="_search_name")
    hotel_ids = fields.Many2many(string="Hotel", comodel_name="hotel.hotel")
    assigned_to = fields.Many2one(string="Assgned to", comodel_name="res.users", domain=lambda self: [('groups_id', 'in', [self.env.ref('Hotel-Management-Odoo.group_employee').id])])
    number_of_hotels = fields.Integer(string="Hotels", compute="_compute_number_of_hotels")

    @api.depends("hotel_ids")
    def _compute_number_of_hotels(self):
        for record in self:
            record.number_of_hotels = len(record.hotel_ids)

 
