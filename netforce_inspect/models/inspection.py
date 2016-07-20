import random
import time
import pyqrcode
from datetime import datetime, timedelta

from netforce.model import Model, fields, get_model
from netforce.database import get_active_db
from netforce.access import get_active_user
from .utils import get_random, get_random_ip_address, get_random_max_address

#HOST="http://128.199.71.66:9999"
HOST="http://v5.insspection.com"

class Inspection(Model):
    _name="inspection"
    _field_name="plat_no"
    _key=["plat_no"]

    _fields={
        'number': fields.Char("Number", search=True),
        'plat_no': fields.Char("Plat No", search=True),
        'plat_no2': fields.Char("Plat No2", search=True),
        'ref': fields.Char("Reference"),
        'result_check': fields.Selection([['pass','Pass'],['fail','Fail']], 'Result Check'),
        'sequence_check': fields.Char("Sequence Check"),
        'date': fields.DateTime("Date Check"),
        'number_perm': fields.Char("Number Permission"),
        'location_check_id': fields.Many2One('inspect.location',"Location Check"),
        'owner_perm': fields.Char("Owner Permission"),
        #'date_register': fields.Date("Date Register", search=True),
        'date_register': fields.Char("Date Register", search=True),
        'car_type_id': fields.Many2One("car.type","Car Type"),
        'inspect_type_id': fields.Many2One("inspect.type","Inspect Type"),
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
        'value_volume_level': fields.Char("Value Volume Level"),
        'value_emission': fields.Char("Value Emission"),
        'value_co': fields.Char("Value CO"),
        'value_hc': fields.Char("Value HC"),
        'audit_first': fields.Char("Audi First"),
        'audit_second': fields.Char("Audi Second"),
        'value_light_far_left': fields.Char("Value Light Far Left"),
        'value_light_far_right': fields.Char("Value Light Far Right"),
        'value_light_low_left': fields.Char("Value Light Low Left"),
        'value_light_low_right': fields.Char("Value Light Low Right"),
        'position_light_far_left': fields.Char("Position Light Far Left"),
        'position_light_far_right': fields.Char("Position Light Far Right"),
        'position_light_low_left': fields.Char("Position Light Low Left"),
        'position_light_low_right': fields.Char("Position Light Low Right"),
        'ip_address': fields.Selection([],"IP Address"),
        'max_address': fields.Selection([],"Max Address"),
        'name_tr_au': fields.Char("Name TR-AU"),
        'total_distance': fields.Char("Total Distance"),
        'image': fields.File("Image"),
        #'distance_uom_id': fields.Many2One("uom","Distance UoM"),
        'uom': fields.Selection([['km','km']],"Distance UoM"),
        'no_car_tank': fields.Char("No Car Tank"),
        'break_image': fields.File("Break Image"),
        'kind_car': fields.Char("Kind Car"),
        'color_car': fields.Char("Car Color"),
        'car_proportion': fields.Char("Car Proportion"),
        'no_sit': fields.Char("No Sit"),

        # other
        'password': fields.Char("Password"),
        'qrcode': fields.File("QRCode"),
        'date_print': fields.Date("Date Print", function="_get_all_date", function_multi=True),
        'date_exp': fields.Date("Date Exp"),
        'province_id': fields.Many2One("province","Province"),
        'user_id': fields.Many2One("base.user","User"),
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
        'user_id': lambda *a: get_active_user(),
        'date_exp': lambda *a: (datetime.now()+timedelta(days=90)).strftime("%Y-%m-%d"),
        'uom': 'km',
        'perform_brake': 'pass',
        'perform_brake_hand': 'pass',
        'result_check': 'pass',
        'result_diff': 'pass',
        'result_break': 'pass',
        'result_break_hand': 'pass',
        'result_wheel': 'pass',
        'result_sound': 'pass',
        'result_pullution': 'pass',
        'result_horn': 'pass',
        'result_speedmotor': 'pass',
        'result_lamp_light': 'pass',
        'result_turn_lamp': 'pass',
        'result_plate_lamp': 'pass',
        'result_glass': 'pass',
        'result_steering': 'pass',
        'result_wheel_tires': 'pass',
        'result_tank_pipe': 'pass',
        'result_lower_part': 'pass',
        'result_chassis': 'pass',
        'result_door_floor': 'pass',
        'result_belt': 'pass',
        'result_wiper_motor': 'pass',
        'result_other': 'pass',
    }


    def create(self,vals,**kw):
        allow, limit, count=get_model("limit.inspect").allow_record()
        if not allow:
            raise Exception("Not allow to create record more than %s"%(limit))
        vals['qrcode']=self.gen_qrcode(vals.get("number"), vals.get("password"))
        new_id=super().create(vals,**kw)
        return new_id

    def write(self,ids, vals,**kw):
        super().write(ids, vals,**kw)
        obj=self.browse(ids)[0]
        self.gen_qrcode(obj.number, obj.password)

    def _get_all_date(self, ids, context={}):
        res={}
        date_print=time.strftime("%Y-%m-%d")
        for obj in self.browse(ids):
            if obj.date:
                date_print=obj.date.split(" ")[0]
            res[obj.id]={
                'date_print': date_print,
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

    def view_report(self, ids, context={}):
        obj=self.browse(ids)[0]
        url=HOST+"/inspectionreport/checkqr?id=%s&password=%s"%(obj.number, obj.password)
        print('URL ', url)
        return {
            'next':{
                'type': 'url',
                'url': url,
            }
        }

    def select_max_address(self,context={}):
        data=context['data']
        count=10
        items=get_random_max_address(count)
        max_address=data.get('max_address')
        if max_address:
            max_selected=(max_address, max_address)
            items.append(max_selected)
        return items

    def select_ip_address(self,context={}):
        data=context['data']
        count=15
        items=get_random_ip_address(count)
        ip_address=data.get('ip_address')
        if ip_address:
            ip_selected=(ip_address,ip_address)
            items.append(ip_selected)
        return items

    def onchange_location_check(self, context={}):
        data=context['data']
        loc_id=data.get("location_check_id")
        if loc_id:
            loc=get_model("inspect.location").browse(loc_id)
            data.update({
                'number_perm': loc.number_perm,
                'owner_perm': loc.owner_perm,
                'audit_first': loc.audit_first,
                'audit_second': loc.audit_second,
                'name_tr_au': loc.name_tr_au,
            })
        return data

    def onchange_inspect_type(self, context={}):
        data=context['data']
        type_id=data['inspect_type_id']
        if type_id:
            type=get_model("inspect.type").browse(type_id)
            data.update({
                'brake_force1_shaft_left': type.brake_force1_shaft_left,
                'brake_force1_shaft_right': type.brake_force2_shaft_right,
                'brake_force2_shaft_left': type.brake_force2_shaft_left,
                'brake_force2_shaft_right': type.brake_force2_shaft_right,
                'brake_force3_shaft_left': type.brake_force3_shaft_left,
                'brake_force3_shaft_right': type.brake_force3_shaft_right,
                'brake_force4_shaft_left': type.brake_force4_shaft_left,
                'brake_force4_shaft_right': type.brake_force4_shaft_right,
                'weight_shaft1': type.weight_shaft1,
                'weight_shaft2': type.weight_shaft2,
                'weight_shaft3': type.weight_shaft3,
                'weight_shaft4': type.weight_shaft4,
                'diff_shaft1': type.diff_shaft1,
                'diff_shaft2': type.diff_shaft2,
                'diff_shaft3': type.diff_shaft3,
                'diff_shaft4': type.diff_shaft4,
                'brake_force_left': type.brake_force_left,
                'brake_force_right': type.brake_force_right,
                'value_co': type.value_co,
                'value_hc': type.value_hc,
                'value_light_far_left': type.value_light_far_left,
                'value_light_far_right': type.value_light_far_right,
                'value_light_low_left': type.value_light_low_left,
                'value_light_low_right': type.value_light_low_right,
                'position_light_far_left': type.position_light_far_left,
                'position_light_far_right': type.position_light_far_right,
                'position_light_low_left': type.position_light_low_left,
                'position_light_low_right': type.position_light_low_right,
            })
        return data

    def onchange_car_type(self, context={}):
        data=context['data']
        data['inspect_type_id']=None
        return data

Inspection.register()
