from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT * FROM usuarios;"
    result = connectToMySQL('mydb').query_db(query)
    return render_template('/index.html', result=result)

@app.route('/insert')
def insert():
    data = {
        "nombre": "Vale",
        "edad": "25",
        "direccion_id": "6"
    }

    query = "INSERT INTO usuarios (nombre, edad, direccion_id) VALUES(%(nombre)s, %(edad)s, %(direccion_id)s);"
    result = connectToMySQL('mydb').query_db(query,data)

    return render_template('/insert.html', result=result)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }

    query = "DELETE FROM usuarios WHERE id = %(id)s;"
    result = connectToMySQL('mydb').query_db(query, data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)