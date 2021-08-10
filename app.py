import os
from api import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module, __name__)

if __name__ == '__main__':
    app.run()