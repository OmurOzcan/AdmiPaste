# -*- coding: utf-8 -*-

from admipaste import app, database
from flask import request, redirect
import json


@app.route('/api/submit', methods=["POST"])
def submit():
    paste = request.form["paste"]
    user = request.form["user"]

    if request.form["isBrowser"] == "yes":
        return redirect("/paste/%s" % database.save_paste(paste, user))

    return json.dumps({"ok": True, "pasteid": database.save_paste(paste, user)})


@app.route('/api/pastes')
def newest():
    return json.dumps({"ok": True, "pastes": database.get_newest(20)})


@app.route('/api/pastes/<string:pasteid>')
def get(pasteid):
    return json.dumps({"ok": True, "paste": database.get_paste(pasteid)})
