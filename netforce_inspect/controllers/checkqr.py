from netforce.controller import Controller
from netforce.template import render
#from netforce import config
from netforce.database import get_connection
#from netforce import access
#from netforce import config
from netforce.model import get_model

class CheckQR(Controller):
    _path="/inspectionreport/checkqr"

    def get(self):
        #url="https://v5.inspection.in.th/inspectionreport/checkqr?id=1541844&password=f45681f1"
        db=get_connection() # prevent to error get transaction
        try:
            db.begin()
            id=self.get_argument("id")
            password=self.get_argument("password")
            data={
                'id': id,
                'password': password,
            }
            res=get_model("inspection").search_read([])
            if res:
                data['obj']=res[-1]
            html=render("checkqr",data)
            self.write(html)
        except Exception as e:
            self.write("ERROR : %s"%str(e))
        finally:
            if db:
                db.commit()

CheckQR.register()
