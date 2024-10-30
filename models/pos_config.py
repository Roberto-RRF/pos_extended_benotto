from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    region = fields.Char(string="Region")