from odoo import models, fields

class rooms(models.Model):
    _name = "rooms"
    _description = "room details for a hotel"

    name = fields.Char('Room name/number',required=True)
    selling_price = fields.Float('Sale price per unit',default='0.0',required=True)
    cost = fields.Float('Cost price per unit',default='0.0',required=True)
    