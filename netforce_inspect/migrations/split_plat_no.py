from netforce.model import get_model
from netforce import migration
from netforce.access import set_active_user

class Migration(migration.Migration):
    _name="split.plat.no"
    _version="3.1.3"

    def migrate(self):
        set_active_user(1)
        for inspect in get_model("inspection").search_browse([]):
            plat_no=inspect.plat_no or ""
            items=[item for item in plat_no.split(" ") if item]
            if len(items)==2:
                inspect.write({
                    'plat_no': items[0],
                    'plat_no2': items[1],
                })

Migration.register()
