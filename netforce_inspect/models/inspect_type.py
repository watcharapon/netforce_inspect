from netforce.model import Model, fields

class InspectType(Model):
    _name="inspect.type"
    _string="Inspect Type"

    _fields={
        'name': fields.Char("Name", required=True, search=True),
    }

InspectType.register()
