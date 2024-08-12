from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        return num1 % num2
    else:
        return "Invalid operation"

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']
    result = calculate(num1, num2, operation)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
