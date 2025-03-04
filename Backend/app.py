from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    with open('analyzed_data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
