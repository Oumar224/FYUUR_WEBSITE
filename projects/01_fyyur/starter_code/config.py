import os
from dotenv import load_dotenv

load_dotenv()
username=os.getenv("USER_NAME")
password=os.getenv("PASSWORD")
ip_adresse=os.getenv("IP_ADRESSE")
port=os.getenv("PORT")
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#enable track modification
SQLALCHEMY_TRACK_MODIFICATIONS=True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI ='postgresql://{}:{}@{}:{}/musiccatalogue'.format(username , password , ip_adresse , port)
SQLALCHEMY_DATABASE_URI ='postgres://dfzapurqsgmlww:b9a9691bf5b6520018ebb845ae3bb1b372def0158954a9092318a578b15049bd@ec2-44-209-186-51.compute-1.amazonaws.com:5432/d2qrlqdvkv40ee'


#search index baseapp
# WHOOSH_BASE='whoosh'
