from app.ext import db
import datetime
from utils.mixins import DictMixin
from flask import current_app
from utils.time_utils import now

        
class Script(DictMixin, db.Model):
    
    __tablename__ = 'script'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_time = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    path = db.Column(db.String(256))
    paras = db.Column(db.JSON)
    r_type = db.Column(db.String(64))
    description = db.Column(db.String(512))




# class Workflow(DictMixin, db.Model):

#     __tablename__ = 'workflow'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     path = db.Column(db.String(1024))
#     paras = db.Column(db.String(256))


# class Script(DictMixin, db.Model):

#     __tablename__ = 'script'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     path = db.Column(db.String(512))
    # description = db.Column(db.Text)

    # paras = db.Column(db.JSONB)
