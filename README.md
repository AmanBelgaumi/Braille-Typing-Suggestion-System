# 🔠 Braille Autocorrect App (QWERTY Braille Typing)

A real-time web app that lets users type Braille using QWERTY key combos (e.g., D + Q + O for 'o') and get accurate word suggestions using similarity-based autocorrection.

---

## 🌐 Live Demo

👉 [Visit the Live App](https://braille-typing-suggestion-system.onrender.com/)

---

## 🧠 Features

- Type Braille using custom QWERTY key combinations.
- Autocorrects Braille-typed words in real time.
- Displays word suggestions for easy correction.
- Allows sentence construction word-by-word.
- Responsive UI with mouse-click suggestion selection.

---

## 💡 How It Works

- **Key Mapping:** Keys like `D`, `W`, `Q`, `K`, `O`, `P` are mapped to Braille dots 1–6.
- **Translation:** Typed key combinations are matched to Braille letters.
- **Autocorrect:** Uses dot-pattern similarity to suggest closest English words from a dictionary.
- **Dictionary:** Based on Oxford 3000 words (customizable).

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** Vanilla JS, HTML, CSS
- **Hosting:** [Render.com](https://render.com)

---

## 📦 File Structure

├── app.py # Flask server

├── requirements.txt # Python dependencies

├── oxford_3000.txt # Dictionary file

├── templates/
      
      └── index.html # Main frontend UI

├── static/ # (Optional) CSS or JS files

└── README.md # Project documentation
