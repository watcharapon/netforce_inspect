from netforce.model import Model, fields

class CarLocation(Model):
    _name="car.location"
    _fields={
        'name': fields.Char("Name", required=True, search=True),
    }

CarLocation.register()
