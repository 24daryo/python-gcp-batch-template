import os
from flask import Flask

from database import db_session
from models import User
import configs as C

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
   # これがないとbroken pipeエラーになる
   db_session.remove()

@app.route("/test", methods=["GET"])
def test():
    user = User.query.filter(User.name == 'admin').first()
    if user:
        return user.email
    return "Not Found"

@app.route("/")
def hello_world():
   name = os.environ.get("TEST_VARIABLE", "Failed")
   return f"Hello World!, Read {name}"

if __name__ == "__main__":
   app.run(debug=True, host=C.SERVER_HOST, port=C.SERVER_PORT)