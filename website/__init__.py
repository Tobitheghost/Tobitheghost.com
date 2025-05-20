from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_cors import CORS

from werkzeug.middleware.proxy_fix import ProxyFix

from .utility.secret import mail_password, mail_username, mail_port, secret_key
from .utility import logs

path_links = []
csrf = CSRFProtect()
mail = Mail()
socketio = SocketIO()
cors = CORS()

def create_app():
    
    # Flask
    app = Flask(__name__)
    # app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = secret_key
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    # Logs
    logs.init_app(app)
    
    # Sockets
    socketio.init_app(app)
    
    # Forms
    csrf.init_app(app)
    
    # Cors
    cors.init_app(app)
    app.config['CORS_ORIGINS'] = '*'
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
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
    
    # from .utility.views import utility
    # app.register_blueprint(utility, url_prefix="/utility")
    
    from .email_templates.views import email
    app.register_blueprint(email, url_prefix="/email")
    
    from .parcel_viewer.views import parcel_viewer
    app.register_blueprint(parcel_viewer, url_prefiix='/parcel_viewer')
    csrf.exempt(parcel_viewer)
    
    from .errors import error
    app.register_blueprint(error)

    return app

if __name__ == '__main__':
    create_app()