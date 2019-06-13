from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())

    MYSQL_HOST = getenv('DB_HOST')
    MYSQL_PORT = int(getenv('DB_PORT'))
    MYSQL_USER = getenv('DB_USER')
    MYSQL_PASSWORD = getenv('DB_PASSWORD')
    MYSQL_DB = getenv('DB_NAME')

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
