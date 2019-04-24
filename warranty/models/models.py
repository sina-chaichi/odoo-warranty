# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Register(models.Model):
    _name = 'warranty.register'
    _description = 'Register warranty type'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    warranty_type = fields.Selection([('type 1','Check'),
                            ('type 2','Promissory Note'),
                            ('type 3','Bank Guarantee')],
                             string='Warranty Type', default='Check')

    # warranty_state = fields.Selection([('state 1','Preparing'),
    #                                       ('state 2','Active'),
    #                                      ('state 3','Expired'),
    #                                      ('state 4', 'Refunded')],
    #                                string='Warranty State', default='Preparing')

    warranty_state = fields.Many2one('warranty.state',
            ondelete='cascade', string='State', required=True)

    date_start = fields.Date(string='Warranty Since:')
    date_end = fields.Date(string='Warranty Until:')

    customer = fields.Many2one('warranty.customer',
        ondelete='cascade', string="Customer", required=True)

    provider = fields.Many2one('warranty.provider',
        ondelete='cascade', string="Provider", required=True)

    release = fields.Boolean(string='Release State', default=False)


class State(models.Model):
    _name = 'warranty.state'
    _description = 'Defining Warranty State by Users'

    state_name = fields.Char(string="State", required=True)
    description = fields.Text()



class Customer(models.Model):
    _inherit = 'res.partner'
    _name = 'warranty.customer'
    _description = 'Customer of contraction'

    warranty_ids = fields.One2many(
        'warranty.register', 'customer', string="Registered Warranties")


class Provider(models.Model):
    _inherit = 'res.users'
    _name = 'warranty.customer'
    _description = 'Customer of contraction'

    warranty_ids = fields.One2many(
        'warranty.register', 'customer', string="Registered Warranties")
