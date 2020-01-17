#from api import app
from flask import Flask
from routes.routes import main
# views, son las rutas de la API

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/v1')
