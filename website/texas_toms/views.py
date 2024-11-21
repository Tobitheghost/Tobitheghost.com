from flask import render_template, Blueprint, request, session, current_app
import logging

logger = logging.getLogger('views')
texas_toms = Blueprint('texas_toms',__name__,template_folder="templates",static_folder="static")
    
@texas_toms.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

@texas_toms.route('/', methods=('GET', 'POST'))
def index():
    return render_template("texas_toms/texas_toms.html")