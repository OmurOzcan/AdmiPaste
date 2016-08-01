from flask import render_template, session, redirect
from admipaste import app, database


@app.route('/')
def index():
    return render_template("index.html", is_index=True)


@app.route('/paste/')
def paste():
    return render_template("pastelist.html", pastes=database.get_newest(20), count=20)


@app.route('/paste/<string:pasteid>')
def register(pasteid):
    return render_template("paste.html", paste=database.get_paste(pasteid))