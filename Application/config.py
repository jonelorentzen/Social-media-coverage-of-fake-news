import os

# contains application-wide configuration, and is loaded in __init__.py

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret' # TODO: Use this with wtforms
    DATABASE = 'database.db'
    UPLOAD_PATH = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16*1024*1024
    #Ensure correct MAX_CONTENT_LENGTH to limit people from uploading files greater than 16MiB
    #This is not possible to flash a warning about, as the connection will be terminated once the filesize exceedes the threshold