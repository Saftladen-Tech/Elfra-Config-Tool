from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sehr_wichtiger_schluessel_hier'

from app.routes import index

app.add_url_rule('/', view_func=index)
