from flask import render_template, Blueprint, request, flash, session, current_app
from flask_wtf.csrf import CSRFError
import json

from ..email import check_email
from ..forms import Contact_Me

home = Blueprint('home',__name__,url_prefix="/",template_folder="website\main\templates")

@home.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(json.dumps(
    [{"request": request.url},
    {"user_agent": str(request.user_agent)},
    {"proxy_ip": request.remote_addr},
    {"forwarded_for": request.headers.get("X_FORWARDED_FOR", default=None)}, 
    {"real_ip": request.headers.get("X_REAL_IP", default=None)}, 
    {"host": request.headers.get("HOST", default=None)}]
    ))
    
@home.route('/', methods=('GET', 'POST'))
def homepage():
    form = Contact_Me()
    response = None
    if request.method == "POST":
        if form.validate_on_submit():
            response = check_email(form.name.data, form.textarea.data, form.email.data, form.test.data)
            resonse_log = {
            "response": response,
            "name": form.name.data,
            "email_msg": form.textarea.data,
            "email": form.email.data,}
            current_app.logger.debug(resonse_log)
        else:
            response = "There seems to be an error with your connection" ,"error"
            resonse_log = {
            "response": response,
            "name": form.name.data,
            "email_msg": form.textarea.data,
            "email": form.email.data,}
            current_app.logger.error(resonse_log)
        session["name"] = form.name.data
        session["email"] = form.email.data
        flash(response)
        print(response)
        return render_template("main/main.html", form=form, response=response)
    return render_template("main/main.html", form=form, response=response)

@home.route('/portfolio', methods=('GET', 'POST'))
def portfolio():
    return render_template("main/menu_grid.html")

@home.route('/styles', methods=('GET', 'POST'))
def styles():
    return render_template("main/styles.html")

#Errors
@home.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/csrf_error.html', reason=e.description, handler=True), 400