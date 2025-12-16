from flask import Flask, jsonify, request
import random

app = Flask(__name__)

jokes_db = [
    {"id": 1, "joke": "Why don't scientists trust atoms? Because they make up everything!", "category": "science"},
    {"id": 2, "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!", "category": "pun"},
    {"id": 3, "joke": "What do you call a fake noodle? An impasta!", "category": "food"},
    {"id": 4, "joke": "Why don't skeletons fight each other? They don't have the guts.", "category": "halloween"},
    {"id": 5, "joke": "What do you call a bear with no teeth? A gummy bear!", "category": "animal"}
]

@app.route('/')
def root():
    return jsonify({
        "message": "Welcome to Flask Joke API",
        "endpoints": ["/jokes", "/jokes/<id>", "/jokes/random"]
    })

@app.route('/jokes', methods=['GET'])
def get_all_jokes():
    category = request.args.get('category')
    if category:
        filtered = [j for j in jokes_db if j["category"] == category]
        return jsonify(filtered)
    return jsonify(jokes_db)

@app.route('/jokes/<int:joke_id>', methods=['GET'])
def get_joke(joke_id):
    for joke in jokes_db:
        if joke["id"] == joke_id:
            return jsonify(joke)
    return jsonify({"error": "Joke not found"}), 404

@app.route('/jokes/random', methods=['GET'])
def get_random_joke():
    return jsonify(random.choice(jokes_db))

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "framework": "Flask"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)