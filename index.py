import requests
import xmltodict
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def mostrar_tabla():
    # Hacer una solicitud a la API
    url_api = 'URL_DE_LA_API_AQUI'
    response = requests.get(url_api)