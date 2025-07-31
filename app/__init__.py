from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sehr_wichtiger_schluessel_hier'

from app import routes