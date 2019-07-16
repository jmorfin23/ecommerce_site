import os
#doesnt go into git hub because it holds important info.
class Config():
    #environent.get will look at the environment variables and see if the secret-key is included, it will use that value if so.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
