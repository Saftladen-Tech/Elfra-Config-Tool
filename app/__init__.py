from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sehr_wichtiger_schluessel_hier'
csrf = CSRFProtect(app)

from app.routes import index

app.add_url_rule('/', view_func=index)
