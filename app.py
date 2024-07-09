from flask import Flask
import pymysql

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'database': 'FLASK_TEST'
}

@app.route('/')
def hello():
    try:
        connection = pymysql.connect(**db_config)
        connection.close()
        return "¡Todo correcto!, ¡Conexión a la base de datos exitosa!"
    except pymysql.MySQLError as e:
        return f"Error en la conexión a la base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
