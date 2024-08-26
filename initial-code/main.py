# main.py

from flask import Flask, request, jsonify
import calculator_module

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        first_number = data.get('num1')
        second_number = data.get('num2')
        operation = data.get('op')

        if first_number is None or second_number is None or operation is None:
            return jsonify({"error": "Missing parameters"}), 400

        # Convert numbers to float
        first_number = float(first_number)
        second_number = float(second_number)

        # Perform calculation
        result = calculator_module.calculate(first_number, second_number, operation)

        return jsonify({"result": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
