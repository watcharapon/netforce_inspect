from netforce.model import Model, fields

class InspectLocation(Model):
    _name="inspect.location"
    _string="Inspect Location"
    _fields={
        'name': fields.Char("Name", required=True, search=True),
        'number_perm': fields.Char("Number Permission"),
        'owner_perm': fields.Char("Owner Permission"),
        'audit_first': fields.Char("Audi First"),
        'audit_second': fields.Char("Audi Second"),
        'name_tr_au': fields.Char("Name TR-AU"),
    }

InspectLocation.register()
