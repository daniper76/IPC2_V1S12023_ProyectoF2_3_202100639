from flask import Flask, jsonify
from flask import request #pip install flask
import json
app = Flask(__name__)

@app.route('/obtenerUsuarios', methods=['GET'])
def obtenerUsuarios():
    try:
        if request.method == 'GET':
            retorno = { 
                        "usuario": [ 
                            { 
                                "rol": "cliente", 
                                "nombre": "Javier", 
                                "apellido": "Mendizabal", 
                                "telefono": "123456789", 
                                "correo": "javier@cliente.com", 
                                "contrasena": "password1" 
                            }, 
                            { 
                                "rol": "administrador", 
                                "nombre": "Rodrigo", 
                                "apellido": "Arriaga", 
                                "telefono": "987654321", 
                                "correo": "rodrigo@admin.com", 
                                "contrasena": "password2" 
                            }, 
                            { 
                                "rol": "cliente", 
                                "nombre": "Hanna", 
                                "apellido": "Arriaga", 
                                "telefono": "987654321", 
                                "correo": "hanna@cliente.com", 
                                "contrasena": "password3" 
                            }
                        ] 
                    } 
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


@app.route('/obtenerPeliculas', methods=['GET'])
def obtenerPeliculas():
    try:
        if request.method == 'GET':
            retorno = {
                "categoria": [
                {
                    "nombre": "Aventura",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Las momias del faraon",
                                "director": "Luc Besson",
                                "anio": "2010",
                                "fecha": "2023-02-05",
                                "hora": "19:30",
                                "imagen": "https://es.web.img2.acsta.net/medias/nmedia/18/78/77/56/19477844.jpg",
                                "precio": "52"
                            },
                            {
                                "titulo": "Aladdin",
                                "director": "Chad Stahelski",
                                "anio": "2019",
                                "fecha": "2023-06-06",
                                "hora": "20:00",
                                "imagen": "https://m.media-amazon.com/images/M/MV5BMjQ2ODIyMjY4MF5BMl5BanBnXkFtZTgwNzY4ODI2NzM@._V1_FMjpg_UX1000_.jpg",
                                "precio": "55"
                            }
                        ]
                    }
                },
                {
                    "nombre": "Infantil",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Sing 2",
                                "director": "Garth Jenningsr",
                                "anio": "2021",
                                "fecha": "2023-04-05",
                                "hora": "14:30",
                                "imagen": "https://www.universalpictures.com.ar/tl_files/content/movies/sing2/posters/01.jpg",
                                "precio": "75"
                            },
                            {
                                "titulo": "spirited away",
                                "director": "Hayao Miyazaki",
                                "anio": "2001",
                                "fecha": "2023-07-07",
                                "hora": "21:15",
                                "imagen": "https://cinematecadebogota.gov.co/sites/default/files/styles/318_x_460/public/afiches/screen_shot_2021-07-30_at_4.18.59_pm.png?itok=9pijB2o2",
                                "precio": "82"
                            }
                        ]
                    }
                    }
            ]}
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/obtenerSalas', methods=['GET'])
def obtenerSalas():
    try:
        if request.method == 'GET':
            retorno = { 
                "cine": { 
                    "nombre": "Cine ABC", 
                    "salas": { 
                        "sala": [ 
                            { 
                                "numero": "sala3", 
                                "asientos": "100" 
                            }, 
                            { 
                                "numero": "sala4", 
                                "asientos": "80" 
                            }, 
                            { 
                                "numero": "sala5", 
                                "asientos": "120" 
                            } 
                        ] 
                    } 
                } 
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

@app.route('/obtenerTarjetas', methods=['GET'])
def obtenerTarjetas():
    try:
        if request.method == 'GET':
            retorno = { 
                "tarjeta": [ 
                    { 
                        "tipo": "Debito", 
                        "numero": "1234567123456", 
                        "titular": "Rodrigo Arriaga", 
                        "fecha_expiracion": "12/2024" 
                    }, 
                    { 
                        "tipo": "Credito", 
                        "numero": "983210987654", 
                        "titular": "Hanna Arriaga", 
                        "fecha_expiracion": "08/2023" 
                    }, 
                    { 
                        "tipo": "Credito", 
                        "numero": "98321093387654", 
                        "titular": "Flor Mendizabal", 
                        "fecha_expiracion": "04/2023" 
                    }
                ] 
            } 
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)