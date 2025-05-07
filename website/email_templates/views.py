from flask import render_template, Blueprint, request, session, current_app
import logging

logger = logging.getLogger('views')
email = Blueprint('email',__name__,template_folder="templates",static_folder="static")
    
@email.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

@email.route('/', methods=('GET', 'POST'))
def index():
    return render_template("email_templates/layouts/index.html")

@email.route('/template/tobi', methods=('GET', 'POST'))
def templte_one():
    return render_template("email_templates/emails/email_base.html")

@email.route('/template/naruto_x_tmnt', methods=('GET', 'POST'))
def templte_two():
    return render_template("email_templates/emails/naruto_x_tmnt_abandoned_cart.html")