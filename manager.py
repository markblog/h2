from flask import Flask
from flask_cors import CORS
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask import render_template

from app import create_app
from app.ext import db

application = create_app()



manager = Manager(application)
migrate = Migrate(application, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver',Server(port=5555))





if __name__ == "__main__":
    manager.run()


