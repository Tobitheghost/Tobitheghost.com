from flask import render_template, Blueprint, request, session, current_app
import logging

logger = logging.getLogger('views')
javascript_counter = Blueprint('javascript_counter',__name__,template_folder="templates",static_folder="static")
    
@javascript_counter.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

@javascript_counter.route('/', methods=('GET', 'POST'))
def index():
    return render_template("javascript_counter/javascript_counter.html")