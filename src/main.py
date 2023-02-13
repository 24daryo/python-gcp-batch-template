import os
# from flask import Flask
import dotenv
dotenv.load_dotenv()

# from database import db_session
# from models import User
import requests

# app = Flask(__name__)

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#    # broken pipe error防止
#    db_session.remove()

# @app.route("/test", methods=["GET"])
# def test():
#     user = User.query.filter(User.name == 'admin').first()
#     if user:
#         return user.email
#     return "Not Found"

# @app.route("/")
# def hello_world():
#    return f"Hello World!"

# @app.route("/message")

def message():
   LINE_NOTIFY_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')
   LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'
   headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
   data = {'message': '通知成功！'}
   requests.post(LINE_NOTIFY_API, headers=headers, data=data)
   return "通知成功！"

if __name__ == "__main__":
   message()
   # app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 8080)))