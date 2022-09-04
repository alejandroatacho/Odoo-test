# my.part.timers.model
from odoo import models, fields


class my_part_timers(models.Model):
    _name = 'my.part.timers'
    _description = 'My Part Timers'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Name must be unique!"),
    # ]
