from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class NumberRequested(db.Model):
    __tablename__ = 'number_requested'

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    number_requested = db.Column(db.Integer)
    result = db.Column(db.Integer)
