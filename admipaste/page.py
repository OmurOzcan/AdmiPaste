# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, request
from admipaste import app, database


@app.route('/')
def index():
    return render_template("index.html", error=request.args.get("error"),
                           dark=(request.cookies.get('darkTheme') == "yes"))


@app.route('/paste/')
def paste():
    return render_template("pastelist.html", pastes=database.get_newest(20),
                           count=20, dark=(request.cookies.get('darkTheme') == "yes"))


@app.route('/paste/<string:pasteid>')
def register(pasteid):
    return render_template("paste.html", paste=database.get_paste(pasteid),
                           dark=(request.cookies.get('darkTheme') == "yes"))