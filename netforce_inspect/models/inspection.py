import time
import pyqrcode

from netforce.model import Model, fields
from netforce.database import get_active_db
from .utils import get_random

HOST="http://128.199.71.66:9999"

class Inspection(Model):
    _name="inspection"
    _name_field="number"
    _key=["number"]

    _fields={
        'number': fields.Char("Number", search=True),
        'ref': fields.Char("Reference"),
        'result_check': fields.Selection([['pass','Pass'],['fail','Fail']], 'Result Check'),
        'sequence_check': fields.Char("Sequence Check"),
        'date': fields.DateTime("Date Check"),
        'number_perm': fields.Char("Number Permission"),
        'location_check': fields.Char("Location Check"),
        'owner_perm': fields.Char("Owner Permission"),
        'date_register': fields.DateTime("Date Register", search=True),
        'type_car': fields.Char("Type Car"),
        'license_car': fields.Char("License Car"),
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
        'perform_brake': fields.Selection([['pass','Pass'],['fail','Fail']], "Perfomance Brake"),
        'perform_brake_hand': fields.Selection([['pass','Pass'],['fail','Fail']], "Perfomance Brake Hand"),
        'wheel': fields.Char("Wheel"),
        'result_diff': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Difference"),
        'result_break': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Break"),
        'result_break_hand': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Break Hand"),
        'result_wheel': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Wheel"),
        'result_sound': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Sound"),
        'result_pullution': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Pullution"),
        'result_horn': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Horn"),
        'result_speedmotor': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Speed Motor"),
        'result_lamp_light': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Lamp Light"),
        'result_turn_lamp': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Turn Lamp"),
        'result_plate_lamp': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Plate Lamp"),
        'result_glass': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Glass"),
        'result_steering': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Steering"),
        'result_wheel_tires': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Wheel & Tires"),
        'result_tank_pipe': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Tanks & Pipe"),
        'result_lower_part': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Lower Part"),
        'result_chassis': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Chassis"),
        'result_door_floor': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Door Floor"),
        'result_belt': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Belt"),
        'result_wiper_motor': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Wiper Motor"),
        'result_other': fields.Selection([['pass','Pass'],['fail','Fail']], "Result Other"),
        'value_volume_level': fields.Decimal("Value Volume Level"),
        'value_emission': fields.Decimal("Value Emission"),
        'value_co': fields.Decimal("Value CO"),
        'value_hc': fields.Decimal("Value HC"),
        'audit_first': fields.Char("Audi First"),
        'audit_second': fields.Char("Audi Second"),
        'value_light_far_left': fields.Decimal("Value Light Far Left"),
        'value_light_far_right': fields.Decimal("Value Light Far Right"),
        'value_light_low_left': fields.Decimal("Value Light Low Left"),
        'value_light_low_right': fields.Decimal("Value Light Low Right"),
        'position_light_far_left': fields.Decimal("Position Light Far Left"),
        'position_light_far_right': fields.Decimal("Position Light Far Right"),
        'position_light_low_left': fields.Decimal("Position Light Low Left"),
        'position_light_low_right': fields.Decimal("Position Light Low Right"),
        'ip_address': fields.Char("IP Address"),
        'max_address': fields.Char("Max Address"),
        'name_tr_au': fields.Char("Name TR-AU"),
        'total_distance': fields.Decimal("Total Distance"),
        'image': fields.File("Image"),
        'distance_uom_id': fields.Many2One("uom","Distance UoM"),
        'no_car_tank': fields.Char("No Car Tank"),
        'break_image': fields.File("Break Image"),
        'kind_car': fields.Char("Kind Car"),
        'color_car': fields.Char("Car Color"),
        'car_proportion': fields.Decimal("Car Proportion"),
        'no_sit': fields.Decimal("No Sit"),

        # other
        'password': fields.Char("Password"),
        'qrcode': fields.File("QRCode"),
        'date_print': fields.Date("Date Print", function="_get_all_date", function_multi=True),
        'date_exp': fields.Date("Date Exp"),
        'province_id': fields.Many2One("province","Province"),
    }

    def _get_number(self, context={}):
        while 1:
            num=get_random(length=8, only_number=True)
            res=self.search(['password','=', num])
            if not res:
                return num

    def _get_password(self, context={}):
        while 1:
            pwd=get_random()
            res=self.search(['password','=', pwd])
            if not res:
                return pwd

    _defaults={
        'number': _get_number,
        'password': _get_password,
    }

    def create(self,vals,**kw):
        vals['qrcode']=self.gen_qrcode(vals.get("number"), vals.get("password"))
        new_id=super().create(vals,**kw)
        return new_id

    def write(self,ids, vals,**kw):
        super().write(ids, vals,**kw)
        obj=self.browse(ids)[0]
        self.gen_qrcode(obj.number, obj.password)

    def _get_all_date(self, ids, context={}):
        res={}
        datenow=time.strftime("%Y-%m-%d")
        for obj in self.browse(ids):
            res[obj.id]={
                'date_print': datenow,
            }
        return res

    def gen_qrcode(self, id, password):
        print("GENERATE QRCODE!")
        link=HOST+"/inspectionreport/checkqr?id=%s&password=%s"%(id, password)
        url=pyqrcode.create(link)
        fname="%s.png"%(id)
        dbname=get_active_db()
        path="static/db/"+dbname+"/files"
        fpath=path+"/"+fname
        url.png(fpath,scale=8)
        print("FNAME => ", fname)
        return fname

    def do_qrcode(self, ids, context={}):
        obj=self.browse(ids)[0]
        fname=self.gen_qrcode(obj.number, obj.password)
        obj.write({
            'qrcode': fname,
        })
        return {
            'flash': 'QRCode genereate succesfully',
        }

    def view_qrcode(self, ids, context={}):
        obj=self.browse(ids)[0]
        url=HOST+"/inspectionreport/checkqr?id=%s&password=%s"%(obj.number, obj.password)
        print('URL ', url)
        return {
            'next':{
                'type': 'url',
                'url': url,
            }
        }

Inspection.register()
