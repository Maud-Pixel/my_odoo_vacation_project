from odoo import models, fields

class ResPartner(models.Model):
    _inherit="res.partner"

    message_customer = fields.Char(string="Mensonges donnés au client")
    other_informations = fields.Text(string="Commérage sur le client")
    registration = fields.Char(string="Immatriculation")