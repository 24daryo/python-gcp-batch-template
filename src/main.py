import os
import dotenv
dotenv.load_dotenv()

# from database import db_session
# from models import User
import send_message
import storage

def message():
   files = storage.list_files("dev")
   LINE_NOTIFY_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')
   send_message.line(LINE_NOTIFY_TOKEN, str(files))
   send_message.gmail()

if __name__ == "__main__":
   message()