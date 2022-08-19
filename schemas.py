from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import NumberRequested


class NumberRequestedSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = NumberRequested
        load_instance = True
