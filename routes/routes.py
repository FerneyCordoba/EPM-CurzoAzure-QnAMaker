from flask import request
from flask import Blueprint

main = Blueprint('main', __name__)

# Describimos las rutas

# ruta para preguntar
@main.route("/ask", methods=['POST'])
def question():
    question = request.get_json()  # esta orden es para poder hacer post
    return(question)
