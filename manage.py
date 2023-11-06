from app import app
from config import config


config_core = 'development'

if __name__ == '__main__':

    #Manejo archivo config
    app.config.from_object(config[config_core])

    app.run()
