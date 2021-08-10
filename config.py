class Config(object):
    SECRET_KEY = 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:password@localhost/apicocina'