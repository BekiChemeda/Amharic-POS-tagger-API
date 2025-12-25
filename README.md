# 🇪🇹 Amharic POS Tagger API

Hey there! Welcome to the Amharic Part-of-Speech (POS) Tagger API. This project is designed to help you analyze Amharic text by identifying the grammatical roles of each word (like Nouns, Verbs, Adjectives, etc.) using a pre-trained CRF model.

I have built this with **FastAPI** to keep it snappy and modular, making it super easy for you to integrate into your own projects!

---

## 🚀 Getting Started

### 1. Set Up Your Environment
First things first, make sure you have Python installed. Then, grab the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Start It Up!
You can start the server with a simple command:

```bash
python -m app.main
```
The server will start running at `http://localhost:8000`.

---

## 🛠 Features

- **Blazing Fast predictions** using a tuned CRF model.
- **Rate Limiting** built-in (via `slowapi`) to keep things fair and stable.
- **Modular Structure** following industry best practices.
- **Auto-generated Documentation**: Just head over to `/docs` once the server is running.

---

## 📖 API Documentation

### **POS Tagging Endpoint**
**`POST /api/v1/tag`**

Send a JSON body with the text you want to analyze:

**Request:**
```json
{
  "text": "ኢትዮጵያ ታላቅ ሀገር ናት።"
}
```

**Response:**
```json
{
  "tokens": ["ኢትዮጵያ", "ታላቅ", "ሀገር", "ናት", "።"],
  "pos_tags": ["N", "ADJ", "N", "AUX", "PUNC"],
  "tagged_sentence": "ኢትዮጵያ: N\nታላቅ: ADJ\nሀገር: N\nናት: AUX\n።: PUNC\n"
}
```

---

## 🛡 Rate Limiting
To ensure everyone gets a fair share of resources, we've set a default limit of **20 requests per minute**. If you hit this limit, you'll receive a `429 Too Many Requests` response.

---

## 📂 Project Structure
```text
.
├── app/
│   ├── api/          # API endpoints (versioned)
│   ├── core/         # Configuration and settings
│   ├── services/     # Core logic (tokenizer & tagger)
│   └── main.py       # App entry point
├── tuned_crf_pos_tagger.pkl  # The magic model
├── requirements.txt  # Dependencies
└── README.md         # You are here!
```

---

## 🤝 Contributing
Feel free to open an issue or submit a pull request if you have ideas to make this even better!

Made with ❤️ for the Ethiopian NLP community.
