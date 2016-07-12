from netforce.model import Model, fields, get_model
from netforce.access import get_active_user


class LimitInspect(Model):
    _name="limit.inspect"
    _fields={
        'user_id': fields.Many2One("base.user","User"),
        'record_count': fields.Integer("Record Count"),
    }
    
    _defaults={
        'user_id': lambda *a: get_active_user(),
    }

    def increase(self):
        user_id=get_active_user()
        res=self.search_browse([['user_id','=',user_id]])
        count=0
        while not count:
            if res:
                obj=res[0]
                count=(obj.record_count or 0)+1
                obj.write({
                    'record_count': count,
                })
            else:
                count=1
                self.create({
                    'record_count':count,
                })
        return count

    def allow_record(self, context={}):
        user_id=get_active_user()
        user=get_model("base.user").browse(user_id)
        limit=user.limit_inspect or 0
        res=self.search_browse([['user_id','=',user_id]])
        if res:
            obj=res[0]
            count=obj.record_count+1
            if count > limit:
                return False, limit, count
        count=self.increase()
        return True, limit, count

LimitInspect.register()
