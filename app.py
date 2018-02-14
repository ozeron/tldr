from flask import Flask, request
from flask import jsonify
from src.model.summary import build

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(status='OK')

@app.route('/api/summary_from_text', methods=['POST'])
def add_message():
    content = request.get_json()
    text = content['text']
    summary = build(text)
    print(summary)
    return jsonify(text=summary)
