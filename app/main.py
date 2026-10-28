from flask import Flask, jsonify, request
from calculator import add, subtract

app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def menu():
    return jsonify({
        "message": "Welcome to the Calculator Application",
        "options": {
            "1": "Addition",
            "2": "Subtraction"
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
    else:
        return jsonify({"error": "Invalid Choice / Not implemented yet"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
