#coding=utf-8
from flask import render_template, request
from app import app
from crud import CRUD

meta_data = CRUD().meta_data


def basic_structure(name='', location='', search_and=False):

    records = CRUD().find({'name': name, 'location': location, 'search_and': search_and})
    registro = []
    for record in records:
        if CRUD().read(record)[-1] != 1:
            registro.append(CRUD().read(record)[0:6])
    return registro


@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html", title='Home', records=basic_structure(), meta_data=meta_data)


@app.route('/search', methods=['GET'])
def search():
    value_to_search = request.args.get('q').strip()

    return render_template("search.html", title='Busca', records=basic_structure(value_to_search, value_to_search), meta_data=meta_data)


@app.route('/create')
def create():
    meta_data = CRUD().meta_data[0:5]

    return render_template("create.html", title='Criar novo registro', meta_data=meta_data)


@app.route('/create-validation', methods=['POST'])
def validation():
    meta_data = CRUD().meta_data[0:5]
    create = []
    for data in meta_data:
        create.append(str(request.form[data['field_name']]))

    creata = CRUD().create(create)

    return render_template("create.html", title='Validando', meta_data=meta_data, create=creata)


@app.route('/remove', methods=['GET'])
def remove():

    return render_template("delete.html", title='Delete', name=request.args.get('name').strip(), location=request.args.get('location').strip())


@app.route('/remove-validation', methods=['POST'])
def validation_remove():
    record = CRUD().find({'name': request.form['delete-name'], 'location': request.form['delete-location'], 'search_and': True})

    try:
        CRUD().delete(record[0])
        return index()
    except:
        return 'msg - error'


@app.route('/edit', methods=['GET'])
def edit():
    return render_template("edit.html", title='Edit', name=request.args.get('name').strip(), location=request.args.get('location').strip(), meta_data=meta_data)
