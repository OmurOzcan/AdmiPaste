from flask import Flask
import MySQLdb

template_folder = "data/templates"
static_folder = "data/static"

db = None
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


class AdmiPaste:
    def __init__(self, mysql_host, mysql_user, mysql_pass, mysql_name):
        global db
        db = MySQLdb.connect(mysql_host, mysql_user, mysql_pass or "", mysql_name, charset="utf8", init_command="SET NAMES UTF8")

        import admipaste.page
        import admipaste.api

    def run(self, host, port, debug=False):
        app.run(debug=debug, host=host, port=port)
