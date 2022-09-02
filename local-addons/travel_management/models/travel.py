from odoo import models, fields, api


class Travel(models.Model):
    _name = "travel.travel"

    name = fields.char(string="Name", required=True)
    destination = fields.char(string="Destination", required=True)
    start_date = fields.date(string="Start Date", required=True)
    end_date = fields.date(string="End Date", required=True)
