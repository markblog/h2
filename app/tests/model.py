from utils.mixins import DictMixin
from app.ext import db

class Test(DictMixin, db.Model):

    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(256))
