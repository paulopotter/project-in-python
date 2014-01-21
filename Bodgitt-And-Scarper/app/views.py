from flask import render_template
from app import app
from crud import CRUD


@app.route('/')
@app.route('/index')
def index():
    title = 'Home'  # fake user
    meta_data = [{'field_name': '#', 'field_content_length': 1}] + CRUD().meta_data

    records = CRUD().find({'name': '', 'location': '', 'search_and': False})
    registro = []
    for line, record in enumerate(records):
        registro.append([line] + CRUD().read(record)[0:6])

    return render_template("index.html", title=title, records=registro, meta_data=meta_data)
