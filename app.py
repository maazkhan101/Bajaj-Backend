from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    data = request.json.get('data')
    user_id = "maazkhan_2121"
    email = "maazkhan.com"
    roll_number = "FGHH"
    
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
