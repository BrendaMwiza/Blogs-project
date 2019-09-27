import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:mwiza@localhost/blogs'
    SECRET_KEY = "mucyo"
    UPLOADED_PHOTOS_DEST ='app/static/images'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:mwiza@localhost/blogs'

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mwiza:mwiza@localhost/blog_test'


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}