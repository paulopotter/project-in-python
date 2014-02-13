# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app
from crud import CRUD
import json
meta_data = CRUD().meta_data


def basic_structure(name='', location='', search_and=False):
    records = CRUD().find({'name': name, 'location': location, 'search_and': search_and})
    registro = []
    for record in records:
        if CRUD().read(record)[-1] != 1:
            line_record = CRUD().read(record)[0:6]
            strip_record = [x.strip(' ') for x in line_record]
            registro.append(strip_record)
    return registro


@app.route('/')
@app.route('/index')
def index():
    line_record = {}
    for line, record in enumerate(basic_structure()):
        line_record[line] = record

    return render_template("index.html", meta_data=meta_data, line_record=line_record)


@app.route('/search', methods=['GET'])
def search():
    value_to_search = request.args.get('q').strip()
    line_record = {}
    for line, record in enumerate(basic_structure(value_to_search, value_to_search)):
        line_record[line] = record

    return render_template("search.html", meta_data=meta_data, line_record=line_record)


@app.route('/create')
def create():
    meta_data = CRUD().meta_data[0:5]

    return render_template("create.html", meta_data=meta_data)


@app.route('/create-validation', methods=['POST'])
def create_validation():
    meta_data = CRUD().meta_data[0:5]
    create = []
    for data in meta_data:
        value_input = request.form[data['field_name']]
        create.append(value_input)

    reply_create = CRUD().create(create)

    return render_template("create.html", meta_data=meta_data, create=reply_create)


@app.route('/remove', methods=['GET'])
def remove():

    return render_template("delete.html", name=request.args.get('name').strip(), location=request.args.get('location').strip())


@app.route('/remove-validation', methods=['GET'])
def validation_remove():
    record = CRUD().find({'name': request.args.get('name'), 'location': request.args.get('location'), 'search_and': True})

    delete = CRUD().delete(record[0])
    if delete:
        return render_template('delete.html', msg_delete=record)
    else:
        return render_template('delete.html', msg_delete='Registro apagado com sucesso!')


@app.route('/edit', methods=['GET'])
def edit():
    search = CRUD().find({'name': request.args.get('name'), 'location': request.args.get('location'), 'search_and': True})
    recNo = search[0]
    record = CRUD().read(recNo)
    values = []
    for value in record:
        values.append(str(value).strip())

    return ''


@app.route('/edit-me', methods=['GET'])
def edit_validation():
    meta_data = CRUD().meta_data[0:6]
    edit = {}
    id_line = request.args.get('id')
    new_value = request.args.get('val')
    edit['id'] = json.loads(id_line)
    edit['value'] = new_value
    read = CRUD().read(edit['id'][0])
    new_record = {}
    for line, old_record in enumerate(read[:6]):
        if meta_data[line]['field_name'] == edit['id'][1]:
            new_record[meta_data[line]['field_name']] = edit['value']
        else:
            new_record[meta_data[line]['field_name']] = old_record

    CRUD().update(edit['id'][0], new_record)
    return ''
