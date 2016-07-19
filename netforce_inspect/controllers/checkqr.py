from netforce.controller import Controller
from netforce.template import render
from netforce.locale import set_active_locale, get_active_locale
from netforce.database import get_connection
from netforce.model import get_model
from netforce.access import set_active_user
#from netforce_sale.models import utils as sale_utils

class CheckQR(Controller):
    _path="/inspectionreport/checkqr"

    def get(self):
        #url="https://v5.inspection.in.th/inspectionreport/checkqr?id=1541844&password=f45681f1"
        current_local=get_active_locale()
        set_active_user(1) #admin
        set_active_locale('th_TH')
        db=get_connection() # prevent to error get transaction
        try:
            db.begin()
            id=self.get_argument("id")
            if not id:
                self.write("Missing ID")
                return
            password=self.get_argument("password")
            if not password:
                self.write("Missing Password")
                return
            ctx={
                'obj': None,
            }
            #res=db.query("select * from inspection where number=%s and password=%s",id,password)
            dom=[
                ['number','=', id],
                ['password','=', password]
            ]
            res=get_model("inspection").search_read(dom)
            if res:
                #t0=res[-1]['date']
                #t1=t0.split(" ")
                #res[-1]['date']='%s %s'%(sale_utils.date2thai(t1[0], format='%(d)s %(Tm)s %(BY)s'), t1[1])
                #res[-1]['date_register']=sale_utils.date2thai(res[-1]['date_register'], format='%(d)s %(Tm)s %(BY)s')
                ctx['obj']=res[-1]
            else:
                ctx['nothing']=True
            data=ctx['obj']
            html=render("checkqr",context=ctx, data=data)
            self.write(html)
        except Exception as e:
            self.write("ERROR : %s"%str(e))
        finally:
            if db:
                db.commit()
        set_active_locale(current_local)

CheckQR.register()
