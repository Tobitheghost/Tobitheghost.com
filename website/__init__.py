from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_socketio import SocketIO

from .utility.secret import mail_password, mail_username, mail_port, secret_key
from .utility import logs
from . import errors

path_links = []
csrf = CSRFProtect()
mail = Mail()
socketio = SocketIO()

def create_app():
    
    # Flask
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = secret_key
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    logs.init_app(app)
    
    # Sockets
    socketio.init_app(app)
    
    # Forms
    csrf.init_app(app)

    # Errors
    app.register_error_handler(415, errors.unsupported_media_type)
    app.register_error_handler(418, errors.imateapot_error)
    app.register_error_handler(451, errors.unavailable_for_legal_reasons)
    app.register_error_handler(404, errors.page_not_found)
    
    # Email Server
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = mail_port
    app.config["MAIL_USERNAME"] = mail_username
    app.config["MAIL_PASSWORD"] = mail_password
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    mail.init_app(app)
    
    # BluePrints
    from .main.views import home
    app.register_blueprint(home)
    
    from .chat_app.views import chat_app
    app.register_blueprint(chat_app,url_prefix="/chat_app")
    csrf.exempt(chat_app)
    
    from .javascript_counter.views import javascript_counter
    app.register_blueprint(javascript_counter,url_prefix="/javascript_counter")
    
    from .pixel_art.views import pixel_art
    app.register_blueprint(pixel_art, url_prefix="/pixel_art")
    
    from .sourkat.views import sourkat
    app.register_blueprint(sourkat, url_prefix="/sourkat")
    
    from .texas_toms.views import texas_toms
    app.register_blueprint(texas_toms, url_prefix="/texas_toms")
    
    from .parcel_viewer.views import parcel_viewer
    app.register_blueprint(parcel_viewer, url_prefiix='/parcel_viewer')

    return app

if __name__ == '__main__':
    create_app()