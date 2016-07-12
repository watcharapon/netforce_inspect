from netforce.model import Model, fields


class User(Model):
    _inherit="base.user"

    _fields={
        'limit_inspect': fields.Integer("Limit Inspection"),
    }

User.register()
