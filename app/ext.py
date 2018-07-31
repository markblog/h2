from flask_sqlalchemy import SQLAlchemy
from utils.records import Database

db = SQLAlchemy()
raw_db = Database(db)

"""
This should be replaced by the real redis database, so to change it conveniently,
please keep the same grammar with redis
- token_black_list is for logout, due to the defects of the jwt
"""
redis_db = {'token_black_list':[]}
# add db model
from app.user import model
from app.workflow import model
from app.tests import model

