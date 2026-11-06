from flask import Flask, jsonify, render_template, request
import secrets
import string

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate_password():
    data = request.get_json()
    user_input = data.get('words', '')

    raw_words = [w.strip().capitalize() for w in user_input.replace(',', ' ').split()]
    unique_words = list(set(raw_words))

    if len(unique_words) < 3:
        return jsonify({
            "error": "Not enough unique words. Please provide at least 3 distinct words."
        }), 400

    secure_rng = secrets.SystemRandom()
    selected_words = secure_rng.sample(unique_words, k=3)

    digits = [secure_rng.choice(string.digits) for _ in range(2)]
    symbol = secure_rng.choice(list("!@#$%^&*-_"))

    passphrase = "".join(selected_words) + "".join(digits) + symbol
    return jsonify({"password": passphrase})


@app.route('/api/game/validate', methods=['POST'])
def validate_game():
    data = request.get_json()

    new_words = [w.strip().lower() for w in data.get('new_words', []) if w.strip()]
    history = [w.strip().lower() for w in data.get('history', [])]

    if len(new_words) != 3:
        return jsonify({"valid": False, "error": "You must provide exactly 3 words."}), 400

    if len(set(new_words)) != 3:
        return jsonify({"valid": False, "error": "You repeated a word in this submission!"})

    for word in new_words:
        if word in history:
            return jsonify({
                "valid": False,
                "error": f"GAME OVER: You already used the word '{word.capitalize()}' in a previous round!"
            })

    secure_rng = secrets.SystemRandom()
    digits = [secure_rng.choice(string.digits) for _ in range(2)]
    symbol = secure_rng.choice(list("!@#$%^&*-_"))

    passphrase = "".join([w.capitalize() for w in new_words]) + "".join(digits) + symbol

    return jsonify({
        "valid": True,
        "passphrase": passphrase,
        "accepted_words": new_words
    })


if __name__ == '__main__':
    app.run(debug=True)