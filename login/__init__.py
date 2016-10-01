from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/userapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'f15ad4d0afc41062dd570d24c48d8a768febabd2' # Required for session encryption
db = SQLAlchemy(app)

from login import login_views, models
