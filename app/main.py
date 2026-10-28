from flask import Flask, jsonify, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def menu():
    return jsonify({
        "message": "Welcome to the Calculator Application",
        "options": {
            "1": "Addition",
            "2": "Subtraction",
            "3": "Multiplication",
            "4": "Division"
        }
    })

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    choice = data.get('choice')
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    
    if choice == '1':
        return jsonify({"result": add(a, b)})
    elif choice == '2':
        return jsonify({"result": subtract(a, b)})
    elif choice == '3':
        return jsonify({"result": multiply(a, b)})
    elif choice == '4':
        try:
            return jsonify({"result": divide(a, b)})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "Invalid Choice"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
