from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class car(models.Model):
    _name = 'car.car'
    _description = 'car.car'

    name = fields.Char(string="Marque", required=True)
    horse_power = fields.Integer(string="Nombre de chevaux")
    door_number= fields.Float(string="Nombre de portes")
    description = fields.Text()
    driver_id = fields.Many2one("res.partner", string="Driver")
    parking_id = fields.Many2one('parking.parking', string="Parking")
    car_feature_ids = fields.Many2many("car.feature", string="Options(s)")
    driver_message = fields.Char(string="Message au conducteur", compute="say_hello")
    total_speed = fields.Integer(string='Total_speed', compute="get_total_speed")
    status = fields.Selection([("new","New"),("used","Used"),("sold","Sold")],string="Status",default="new")

    @api.model 
    def create(self, values):
        print("Hello Maud")
        if values["name"] == "Coccinelle" :
            values['name'] = "The greatest car of the world !!!!"
        result = super(car,self).create(values)
        return result
    '''
    def write(self,values): 
        if values["horse_power"] == 5:
            raise ValidationError(_("Ca pas être possible !"))
        result = super(car,self).write(values)
        return result
    '''
    def unlink(self):
        for rec in self:
            if rec.name == "Carosse": 
                raise ValidationError(_("On ne supprime pas le carosse de la Princesse :("))
            return super(car,self).unlink()
        

    def set_status_car_new(self):
        self.status = "new"

    def set_status_car_used(self):
        self.status = "used"
    
    def set_status_car_sold(self): #à réparer (ne trouve pas le driver_id)
        self.status = "sold"
        template_id = self.env.ref("garbage_module.car_mail_template")
        if template_id :
            template_id.send_mail(self.id, force_send=True, raise_exception=True, email_values={'email_to': self.driver_id.email})

    def get_total_speed(self):
        self.total_speed=100*self.horse_power

    def say_hello(self):
        self.driver_message = "Hello "+ self.driver_id.name


class parking(models.Model):
    _name = 'parking.parking'

    name = fields.Char(string="Parking")
    car_ids = fields.One2many("car.car", "parking_id", string="Cars")


class CarFeature(models.Model):
    _name="car.feature"
    _description="car_feature"

    name = fields.Char(string="Option(s)")
    

 

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
