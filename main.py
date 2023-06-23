from flask import Flask, render_template, request, redirect, url_for
from models import Tarea
import db

app = Flask (__name__) # En app se encuentra el servidor web Flask

# La barra (/) se conoce como la páqina de inicio (home)
# Definimos para esta ruta, el comportamiento a seguir
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() # Sintaxis para obtener los valores de BD
    # Creamos una variable lista_de_tareas para que cuando ejecute la web envié los valores de la BD al HTML
    return render_template("index.html", lista_de_tareas = todas_las_tareas)


@app.route("/crear-tarea", methods=["POST"])
def crear():
# Tarea es un objeto de la clase Tarea (una instancia de la clase)
    tarea = Tarea(contenido = request.form['contenido_tarea'], hecha = False)
    db.session.add(tarea) # Añade el objeto de Tarea a la base de datos
    db.session.commit()
    return redirect(url_for("home")) # Indicamos que queremos volver a ejecutar home siempre y cuando la web ya se haya cargado anteriormente


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    # Busca dentro de la base de datos, aquel registro cuyo id coincida con el aportado por el parametro de la ruta. Cuando lo encuentra, se elimina
    tarea = db.session.query(Tarea).filter_by(id=int(id))
    tarea.delete()
    db.session.commit() # Aplicamos los cambos
    return redirect(url_for("home")) # Indicamos que queremos volver a ejecutar home siempre y cuando la web ya se haya cargado anteriormente

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Retorna la tarea
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable boolena su valor contraria
    db.session.commit()
    return redirect(url_for("home")) # Indicamos que queremos volver a ejecutar home siempre y cuando la web ya se haya cargado anteriormente


@app.route('/tarea-modificar/<id>', methods=["POST", "GET"])
def modificar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    
    if request.method == 'POST':
        nuevo_contenido = request.form.get('nuevo_contenido')
        tarea.contenido = nuevo_contenido
        db.session.commit()
        return redirect(url_for("home")) # Indicamos que queremos volver a ejecutar home siempre y cuando la web ya se haya cargado anteriormentes
    return render_template("modificar_tarea.html", tarea = tarea)


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    app.run(debug=True, port=5000)  #debug permite los cambios de la web sin necesidad de abrir y cerrar la app