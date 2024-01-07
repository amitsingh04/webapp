import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webapp/")
from wsgi import app as application
#from wsgi import create_app
#wqapplication = create_app()
application.secret_key = ""