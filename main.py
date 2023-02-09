import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv(verbose=True)
app = Flask(__name__)

@app.route("/")
def hello_world():
   name = os.environ.get("TEST_VARIABLE", "Failed")
   return f"Hello World!, Read {name}"

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))