class Config:
    SECRET_KEY='B!1weNAt1t^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG =True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}