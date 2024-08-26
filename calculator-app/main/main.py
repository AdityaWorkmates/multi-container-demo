from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Base URLs for different services
SERVICES = {
    'add': 'http://addition-service:5001/add',
    'sub': 'http://substraction-service:5002/sub',
    'mul': 'http://multiplication-service:5003/mul',
    'div': 'http://division-service:5004/div'
}

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        operation = data.get('operation')
        if operation not in SERVICES:
            return jsonify({"error": "Invalid operation"}), 400

        response = requests.post(SERVICES[operation], json=data)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify(response.json()), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": "An error occurred with the calculator services"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
