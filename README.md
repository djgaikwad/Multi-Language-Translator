# Multilingual Translator 🌍💬

This is a **Flask-based multilingual translation app** powered by the **Hugging Face** `facebook/mbart-large-50-many-to-many-mmt` model.\*\* It allows users to translate between multiple languages, making communication seamless and efficient.

## Features ✨

- Supports multiple languages: **English, Hindi, Japanese, Spanish, French, and German**.
- Uses **English as a bridge** for not well trained language pairs.
- Simple and user-friendly web interface.
- Powered by **Hugging Face Transformers**.
- Lightweight Flask backend for quick deployment.

## Installation & Setup 🚀

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/multilingual-translator.git
cd multilingual-translator
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

### 5️⃣ Run the Flask App

```bash
python app.py
```

The app will be accessible at `http://127.0.0.1:5000/` 🎉

## Usage 📝

1. Open the web app in your browser.
2. Select the **source language** and **target language**.
3. Enter the text you want to translate.
4. Click **Translate** to get the output instantly!

## Project Structure 📚

```
multilingual-translator/
│-- app.py              # Main Flask application
│-- templates/
│   ├── index.html      # Homepage template
│   ├── result.html     # Translation result page
│-- requirements.txt    # Python dependencies
│-- README.md           # Project documentation
```

## Future Improvements 🔥

- Add more languages 🌏
- Implement speech-to-text & text-to-speech 🎧
- Deploy on a cloud platform 🚀

## Contributions 🤝

Feel free to **fork** this repository and submit a pull request. Any contributions are welcome!

## License 📝

This project is **open-source**, and the license can be customized as needed.

---

**Happy Coding! 🚀🌍**

