class Config:
    SECRET_KEY = "B!1weNAt1t^%kvhUI*S^"


class DevelopmentConfig(Config):
    DEBUG = True
    # Configuracion Mysql
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "abc123...."
    MYSQL_DB = "tienda"


config = {"development": DevelopmentConfig, "default": DevelopmentConfig}
