from flask import Flask, jsonify
from config import Config
from models import db, Message

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    return "<h3>Azure Backend Running</h3>"

@app.route("/messages")
def get_messages():
    messages = Message.query.all()
    return jsonify([{"id": m.id, "content": m.content} for m in messages])

@app.route("/health")
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run()
