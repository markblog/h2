# system config
import os
import logging

DEBUG = True
API_PREFIX = 'api/'

SECRET_KEY = os.environ.get('SECRET_KEY') or '0x1092-3dfe834-324few23-342dlej'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_ECHO = False
LOGGING_FORMAT = """[%(levelname)s] - %(asctime)s : %(message)s
%(module)s [%(pathname)s:%(lineno)d]
"""
LOGGING_LOCATION = 'log/debug.log'
LOGGING_LEVEL = logging.DEBUG
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:gxtagging@localhost/workbench'
BASEFILENAME = 'D:\\Workbench\\'
