import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Gives access to the project in any OS we find ourselves in
# allows outside files / folders to be added to the project from
# the base directory.



class Config:
    # sets configuration variables for our flask app here
    # eventually will use hidden variable items - but for now, we'll leave them exposed in config

    SECRET_KEY="You will never guess...."
    DEPLOY_DATABASE_URL = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Above line (17) removes unnecessary output on terminal.
