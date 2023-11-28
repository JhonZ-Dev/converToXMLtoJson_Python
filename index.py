import requests
import xmltodict
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def mostrar_tabla():
    # Hacer una solicitud a la API
    url_api = 'URL_DE_LA_API_AQUI'
    response = requests.get(url_api)
    
     # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta de XML a JSON
        dict_data = xmltodict.parse(response.text)
        json_data = json.dumps(dict_data, indent=2)
        # Renderizar la tabla HTML con Jinja2
        tabla_html = render_template_string(''' 
                                            
                                            <html>
            <head>
                <style>
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }
                    th, td {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <h2>Tabla de Datos</h2>
                <table>
                    <thead>
                        <tr>
                                            
                                            
                                            ''')