from flask import Blueprint, request, session, current_app, redirect, url_for, render_template, flash
from flask_socketio import join_room, leave_room, send
import random
from string import ascii_uppercase

from .. import socketio

chat_app = Blueprint('chat_app',__name__,template_folder="templates",static_folder="static")

rooms = {}

@chat_app.before_request
def send_session():
    session_log = {"Session Log" : [{"request": request.url},{"user_agent": str(request.user_agent)},{"proxy_ip": request.remote_addr}]}
    session["ip"] = request.headers.get("X_REAL_IP")
    session["log"] = (session_log)
    current_app.logger.debug(session)

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

@chat_app.route('/', methods=('GET', 'POST'))
@chat_app.route('/home', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("chat_app/chat_app.html", error="Please Enter a Name.", code=code, name=name)
        
        if join != False and not code:
            return render_template("chat_app/chat_app.html", error="Please Enter a Room Code.", code=code, name=name)
            
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members":0, "messages":[]}
        elif code not in room:
            return render_template("chat_app/chat_app.html", error="Code does NOT exist.", code=code, name=name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("chat_app.room"))
        
                
    return render_template("chat_app/chat_app.html")

@chat_app.route('/room', methods=('GET', 'POST'))
def room():
    room = session.get("room")
    name = session.get("name")
    if room is None or name is None or room not in rooms:
        return redirect(url_for("chat_app.index"))
    return render_template("chat_app/room.html", room=room, name=name, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    
    
@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    rooms[room]["members"] += 1
    send({"name": name, "message": f"has entered the room"}, to=room)
    
    
@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    send({"name": name, "message": f"has left the room"}, to=room)