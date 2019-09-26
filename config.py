import os

class Config:
    SECRET_KEY = "mucyo"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/blog'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}