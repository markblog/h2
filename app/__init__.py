from flask import Flask
# from app.user import user_bp
from app.workflow import workflow_bp
from app.ext import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    # app.register_blueprint(user_bp)
    app.register_blueprint(workflow_bp)
    CORS(app)
    return app



