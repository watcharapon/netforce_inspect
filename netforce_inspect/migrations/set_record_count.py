from netforce.model import get_model
from netforce import migration
from netforce.access import set_active_user

class Migration(migration.Migration):
    _name="set.record.count"
    _version="3.1.2"

    def migrate(self):
        set_active_user(1)
        for user in get_model("base.user").search_browse([]):
            res=get_model("limit.inspect").search([['user_id','=',user.id]])
            if not res:
                insp_ids=get_model("inspection").search([['user_id','=',user.id]])
                get_model("limit.inspect").create({
                    'user_id': user.id,
                    'record_count': len(insp_ids),
                })

Migration.register()
