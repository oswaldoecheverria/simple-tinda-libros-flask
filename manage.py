from app import app
from config import config
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL


config_core = 'development'
csrf=CSRFProtect()

if __name__ == '__main__':

    #Manejo archivo config
    app.config.from_object(config[config_core])
    # CSRF Security 
    csrf.init_app(app)
    app.run()
