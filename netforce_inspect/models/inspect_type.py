from netforce.model import Model, fields

class InspectType(Model):
    _name="inspect.type"
    _string="Inspect Type"

    _fields={
        'name': fields.Char("Name", required=True, search=True),
        'car_type_id': fields.Many2One("car.type","Car Type"),
        'brake_force1_shaft_left': fields.Char("Brake Force Shaft 1 Left"),
        'brake_force1_shaft_right': fields.Char("Brake Force Shaft 1 right"),
        'brake_force2_shaft_left': fields.Char("Brake Force Shaft 2 Left"),
        'brake_force2_shaft_right': fields.Char("Brake Force Shaft 2 right"),
        'brake_force3_shaft_left': fields.Char("Brake Force Shaft 3 Left"),
        'brake_force3_shaft_right': fields.Char("Brake Force Shaft 3 right"),
        'brake_force4_shaft_left': fields.Char("Brake Force Shaft 4 Left"),
        'brake_force4_shaft_right': fields.Char("Brake Force Shaft 4 right"),
        'weight_shaft1': fields.Char("Weight Shaft 1"),
        'weight_shaft2': fields.Char("Weight Shaft 2"),
        'weight_shaft3': fields.Char("Weight Shaft 3"),
        'weight_shaft4': fields.Char("Weight Shaft 4"),
        'diff_shaft1': fields.Char("Different Shaft 1"),
        'diff_shaft2': fields.Char("Different Shaft 2"),
        'diff_shaft3': fields.Char("Different Shaft 3"),
        'diff_shaft4': fields.Char("Different Shaft 4"),
        'brake_force_left': fields.Char("Brake Force Left"),
        'brake_force_right': fields.Char("Brake Force Right"),
        'value_co': fields.Char("Value CO"),
        'value_hc': fields.Char("Value HC"),
        'value_light_far_left': fields.Char("Value Light Far Left"),
        'value_light_far_right': fields.Char("Value Light Far Right"),
        'value_light_low_left': fields.Char("Value Light Low Left"),
        'value_light_low_right': fields.Char("Value Light Low Right"),
        'position_light_far_left': fields.Char("Position Light Far Left"),
        'position_light_far_right': fields.Char("Position Light Far Right"),
        'position_light_low_left': fields.Char("Position Light Low Left"),
        'position_light_low_right': fields.Char("Position Light Low Right"),
    }

InspectType.register()
