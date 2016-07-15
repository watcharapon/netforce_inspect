from netforce.model import Model, fields

class InspectLocation(Model):
    _name="inspect.location"
    _string="Inspect Location"
    _fields={
        'name': fields.Char("Name", required=True, search=True),
    }

InspectLocation.register()
