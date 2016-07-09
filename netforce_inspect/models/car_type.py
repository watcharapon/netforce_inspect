from netforce.model import Model, fields

class CarType(Model):
    _name="car.type"
    _fields={
        'name': fields.Char("Name", required=True, search=True),
    }

CarType.register()
