from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mul', methods=['POST'])
def mul():
    try:
        data = request.json
        first_number = data.get('first_number')
        second_number = data.get('second_number')

        if first_number is None or second_number is None:
            return jsonify({"error": "Missing parameters"}), 400

        result = first_number * second_number
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
