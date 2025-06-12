from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración directa de conexión a MySQL (RDS)
db_config = {
    'host': 'demodb.cnpg8tdkfawy.us-east-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'mati',
    'password': 'matidlc2006',
    'database': 'contacto_db'
}

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        # Obtener datos del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        fecha = request.form['fecha']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        # Conectar y guardar en la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        query = """
            INSERT INTO formulario (nombre, correo, telefono, fecha, asunto, mensaje)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos = (nombre, correo, telefono, fecha, asunto, mensaje)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

        return render_template(
    'bienvenida.html',
    nombre=nombre,
    correo=correo,
    telefono=telefono,
    mensaje=mensaje
)

    except mysql.connector.Error as err:
        return f"❌ Error al guardar en la base de datos: {err}"

@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
