from odoo import models, fields

class service(models.Model):
    _name = "service"
    _description = "Services available in hotel"

    name = fields.Char("name", default="cleaning service",required=True)
    cost = fields.Float("Cost per unit", default='0.0', required=True)