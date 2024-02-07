from odoo import models, fields

class reservation(models.Model):
    _name = "reservation"
    _description = "all customer reservation"

    selling_price = fields.Float("unit price",required=True)
    stayFor = fields.Date()