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
SQLALCHEMY_DATABASE_URI ="postgres://yfozkdscwkzprp:92581287dbc5841a3536d35ba84f17add813ba8263e3e8b03185c4f71cafb276@ec2-34-193-44-192.compute-1.amazonaws.com:5432/dd40ick3tgaa2q"


#search index baseapp
# WHOOSH_BASE='whoosh'
