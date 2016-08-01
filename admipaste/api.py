# -*- coding: utf-8 -*-

from admipaste import app, database
from flask import request, redirect
import json


@app.route('/api/submit', methods=["POST"])
def submit():
    paste = request.form["paste"]
    user = request.form["user"]
    language = request.form["language"]

    if request.form["isBrowser"] == "yes":
        if not paste:
            return redirect("/?error=Please fill everything")
        return redirect("/paste/%s" % database.save_paste(paste, user, language))

    if not paste:
        return json.dumps({"ok": False, "reason": "paste_empty"})

    return json.dumps({"ok": True, "pasteid": database.save_paste(paste, user, language)})


@app.route('/api/pastes')
def newest():
    return json.dumps({"ok": True, "pastes": database.get_newest(20)})


@app.route('/api/pastes/<string:pasteid>')
def get(pasteid):
    return json.dumps({"ok": True, "paste": database.get_paste(pasteid)})
