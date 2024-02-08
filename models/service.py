# -*- coding: utf-8 -*-

from odoo import models, fields

class service(models.Model):
    _name = "hotel.service"
    _description = "Services available in hotel"
    _check_company_auto = True

    company_id = fields.Many2one("res.company", store=True, copy=False, string="Company",
                                default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one("res.currency", string="Currency", related="company_id.currency_id", default=lambda
                                self: self.env.user.company_id.currency_id.id)
    cost = fields.Monetary(string="Cost per unit")
    name = fields.Char(string="Name", default="cleaning service", required=True, search="_search_name")
    hotel = fields.Many2many(string="Hotel", comodel_name="hotel.hotel")

    def _search_name(self,operator,value):
        return[("Res_name",operator,value)]
