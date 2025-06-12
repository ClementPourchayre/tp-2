from flask import Flask
from app.utils import get_message

app = Flask(__name__)

@app.route('/')
def home():
    return get_message()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
