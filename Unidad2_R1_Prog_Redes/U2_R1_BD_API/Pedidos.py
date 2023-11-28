# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
#Alan Francisco Emmanuel Aguilar Fuentes
# Profesor: Gabriel Barrón R.

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crudr1.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pedidos')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Pedidos(producto, cantidad, precio, usuario_id, fecha_pedido) VALUES(?, ?, ?, ?, ?)'
    cursor.execute(insert, [record['producto'], record['cantidad'], record['precio'], record['usuario_id'], record['fecha_pedido']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Pedidos WHERE correo= ?'
    cursor.execute(delete, [record['producto']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Pedidos SET correo = ? WHERE id= ?'
    cursor.execute(update, [record['producto'], record['cantidad']])
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
