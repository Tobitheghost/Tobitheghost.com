from flask import render_template, Blueprint, request, session, current_app, redirect
import logging

logger = logging.getLogger('views')
sourkat = Blueprint('sourkat',__name__,template_folder="templates",static_folder="static")
    
@sourkat.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

@sourkat.route('/', methods=('GET', 'POST'))
def index():
    return render_template("sourkat/sourkat.html")
    # return redirect("http://www.asourkat.com", code=301)