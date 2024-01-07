import sys
import logging
from webapp import app as application
from webapp import create_app
application = create_app()
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,”/var/www/FlaskApp/”)
application.secret_key = ‘Xopetyn&2345chspgh!’