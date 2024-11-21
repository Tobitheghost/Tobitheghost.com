from flask import render_template, Blueprint, request, session, current_app
import logging

logger = logging.getLogger('views')
pixel_art = Blueprint('pixel_art',__name__,template_folder="templates",static_folder="static")
    
@pixel_art.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

@pixel_art.route('/', methods=('GET', 'POST'))
def index():
    return render_template("pixel_art/pixel_art.html")