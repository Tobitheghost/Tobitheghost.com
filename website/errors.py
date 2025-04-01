import werkzeug
import werkzeug.exceptions
from flask import render_template, Blueprint
from flask_wtf.csrf import CSRFError

error = Blueprint('error',__name__,url_prefix="/",)

@error.app_errorhandler(werkzeug.exceptions.UnsupportedMediaType)
def unsupported_media_type(e):
    return render_template("errors/unsupported_media_type_error.html", reason=e.description, handler=True, code=415), 415

@error.app_errorhandler(werkzeug.exceptions.ImATeapot)
def imateapot_error(e):
    return render_template("errors/im_a_teapot_error.html", reason=e.description, handler=True, code=418), 418

class YouGotHigh(werkzeug.exceptions.HTTPException):
    code = 420
    description = "You are trying to submit a request while high"

@error.app_errorhandler(YouGotHigh)
def weed_error(e):
    return render_template("errors/weed_420_error.html", reason=e.description, handler=True, code=420), 420

@error.app_errorhandler(werkzeug.exceptions.UnavailableForLegalReasons)
def unavailable_for_legal_reasons(e):
    return render_template("errors/unavailable_for_legal_reasons_error.html", reason=e.description, handler=True, code=451), 451

class InfiniteLoop(werkzeug.exceptions.HTTPException):
    code = 508
    description = "You have entered an Infinite Loop"

@error.app_errorhandler(InfiniteLoop)
def infinite_loop_error(e):
    return render_template("errors/infinite_loop_error.html", reason=e.description, handler=True, code=508), 508

@error.app_errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(e):
    return render_template("errors/error.html", reason=e.description, handler=True, code=404), 404

@error.app_errorhandler(werkzeug.exceptions.BadRequest)
def bad_request(e):
    return render_template("errors/error.html", reason=e.description, handler=True, code=400), 400

@error.app_errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/csrf_error.html', reason=e.description, handler=True), 400

