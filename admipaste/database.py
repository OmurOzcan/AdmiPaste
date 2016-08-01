# -*- coding: utf-8 -*-

from admipaste import db
import hashlib


def gen_visid(num_id):
    return hashlib.md5(str(num_id).encode("utf-8")).hexdigest()[-15:]


def get_paste(paste):
    db_cursor = db.cursor()
    db_cursor.execute("SELECT user, paste, lang FROM pastes WHERE vis_id = %s", [paste])

    paste = db_cursor.fetchone()

    if paste is None:
        paste = ("system", "Paste not found", "none")

    db_cursor.close()
    return paste


def save_paste(paste, user, language):
    db_cursor = db.cursor()
    db_cursor.execute("SELECT COUNT(id) FROM pastes")
    pasteid = gen_visid(db_cursor.fetchone()[0] + 1)

    if not user:
        user = "anonymous"

    db_cursor.execute("INSERT INTO pastes(paste, user, vis_id, lang) VALUES (%s, %s, %s, %s)",
                      [paste, user, pasteid, language])
    db.commit()

    db_cursor.close()
    return pasteid


def get_newest(count):
    db_cursor = db.cursor()
    db_cursor.execute("SELECT vis_id, user FROM pastes ORDER BY id DESC LIMIT %s", [count])

    paste = db_cursor.fetchall()

    db_cursor.close()
    return paste


def get_pastes_of(username):
    return None
