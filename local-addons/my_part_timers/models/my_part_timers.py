# my.part.timers.model
from odoo import models, fields


class my_part_timer(models.Model):
    _name = 'my.part.timer'
    _description = 'My Part Timer'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Name must be unique!"),
    # ]
