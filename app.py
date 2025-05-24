from flask import Flask, render_template, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

# Braille mappings
braille_map = {
    'a': {1}, 'b': {1, 2}, 'c': {1, 4}, 'd': {1, 4, 5}, 'e': {1, 5},
    'f': {1, 2, 4}, 'g': {1, 2, 4, 5}, 'h': {1, 2, 5}, 'i': {2, 4}, 'j': {2, 4, 5},
    'k': {1, 3}, 'l': {1, 2, 3}, 'm': {1, 3, 4}, 'n': {1, 3, 4, 5}, 'o': {1, 3, 5},
    'p': {1, 2, 3, 4}, 'q': {1, 2, 3, 4, 5}, 'r': {1, 2, 3, 5}, 's': {2, 3, 4}, 't': {2, 3, 4, 5},
    'u': {1, 3, 6}, 'v': {1, 2, 3, 6}, 'w': {2, 4, 5, 6}, 'x': {1, 3, 4, 6}, 'y': {1, 3, 4, 5, 6},
    'z': {1, 3, 5, 6}
}

# QWERTY to Braille dot mapping
qwerty_to_dot = {'D': 1, 'W': 2, 'Q': 3, 'K': 4, 'O': 5, 'P': 6}

# Load a dictionary of words
def load_dictionary():
    with open("oxford_3000.txt", "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

dictionary = load_dictionary()

# Convert a word into its Braille dot representation
def braille_word_to_dots(word):
    return [braille_map[char] for char in word if char in braille_map]

# Compute similarity between two Braille dot sequences
def similarity(seq1, seq2):
    seq1 = [tuple(sorted(s)) for s in seq1]
    seq2 = [tuple(sorted(s)) for s in seq2]
    return SequenceMatcher(None, seq1, seq2).ratio()

# Route for the main page
@app.route('/')
def index():
    return render_template("index.html")

# Route for suggestions based on Braille-typed word
@app.route('/suggest', methods=['POST'])
def suggest():
    input_text = request.json.get("input", "")
    user_dots = [braille_map[char] for char in input_text if char in braille_map]
    scored = []
    for word in dictionary:
        word_dots = braille_word_to_dots(word)
        score = similarity(user_dots, word_dots)
        if score > 0.5:
            scored.append((word, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    best = scored[0][0] if scored else ""
    suggestions = [w for w, _ in scored[:5]]
    return jsonify(best=best, suggestions=suggestions)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
