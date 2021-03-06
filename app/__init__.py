from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager #for logging in

app = Flask(__name__)

# initialize config variables for application
app.config.from_object(Config)

#bootstrap requires app instance, always comes after app is declared
bootstrap = Bootstrap(app)

#app vaiables for database usage
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#variables for login
login = LoginManager(app)

#when a page requires someone to login, the application will instead rout them to the correct route described below
login.login_view = 'login'

from app import routes


#migrations folder is a repository for your database - where we can go
#back to previous commits of our database
#migrate checks to see if changes occurs in datatable, if it does it creates a new table , but it doesnt use that current commit immediately, so we need to upgrade to use that current 'commit'.
