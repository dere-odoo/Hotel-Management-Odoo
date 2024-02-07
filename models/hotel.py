from odoo import models, fields

class hotel(models.Model):
    _name = "hotel"
    _description = "Hotel specific information"

    name = fields.Char('Name', default="Hotel Name",required=True)
    address = fields.Text("Hotel Address")
    