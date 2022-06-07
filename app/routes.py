from app import app
from flask import render_template

@app.route('/')
def index():
    name = "Vladyslav Zaiets"
    field_of_study = "Applied Informatics"
    group_number = "ZZIAS1-1211"
    return render_template("index.html.jinja", name=name, field_of_study=field_of_study, group_number=group_number)

@app.route('/new')
def new():
    name = "Vladyslav Zaiets"
    field_of_study = "Applied Informatics"
    group_number = "ZZIAS1-1211"
    return render_template("new.html.jinja", name=name, field_of_study=field_of_study, group_number=group_number)