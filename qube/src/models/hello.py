from qube.src.api import persist_db


class Hello(persist_db.Document):
    # Primary ID
    id = persist_db.StringField(required=False)

    # Hello world model data
    name = persist_db.StringField(required=False)
    desc = persist_db.StringField(required=False)

    # Default tracking data
    createdBy = persist_db.StringField(required=False)
    modifiedBy = persist_db.StringField(required=False)
    orgId = persist_db.StringField(required=True)
    tenantId = persist_db.StringField(required=True)
    createdDate = persist_db.StringField(required=False)
    modifiedDate = persist_db.StringField(required=True)
