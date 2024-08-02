from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('passgen.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    data = request.get_json()
    length = int(data['length'])
    password = generate_password(length)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
