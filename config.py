import os
basedir = os.path.abspath(os.path.dirname(__file__))
#doesnt go into git hub because it holds important info.
class Config():
    #environent.get will look at the environment variables and see if the secret-key is included, it will use that value if so.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #uri for sql lite database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    #uri for postgres database connect to local twitter commerce database that we created on pgAdmin

     # 'postgresql://name_of_user:pass_for_user@domain_address:port/name_of_db'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:asdfghjkl;'@localhost:5432/twitter_commerce"
