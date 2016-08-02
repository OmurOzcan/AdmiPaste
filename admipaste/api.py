# -*- coding: utf-8 -*-

from admipaste import app, database
from flask import request, redirect
import json


@app.route("/api")
def docs():
    return redirect("https://github.com/Admicos/AdmiPaste#api-documentation")


@app.route('/api/submit', methods=["POST"])
def submit():
    paste = request.form["paste"]
    user = request.form["user"]
    language = request.form["language"]
    unlist = request.form.get("unlist")

    if unlist is None:
        unlist = False

    if request.form["isBrowser"] == "yes":
        if not paste:
            return redirect("/?error=Please fill everything")
        return redirect("/paste/%s" % database.save_paste(paste, user, language, unlist))

    if not paste:
        return json.dumps({"ok": False, "reason": "paste_empty"})

    return json.dumps({"ok": True, "pasteid": database.save_paste(paste, user, language, unlist)})


@app.route('/api/pastes')
def newest():
    return json.dumps({"ok": True, "pastes": database.get_newest(20)})


@app.route('/api/pastes/<string:pasteid>')
def get(pasteid):
    paste = database.get_paste(pasteid)
    return json.dumps({"ok": paste[3], "paste": paste})
