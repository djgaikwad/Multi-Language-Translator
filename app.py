from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set Hugging Face API Key
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")  # Ensure it's set in the environment

# MBART Model API Endpoint
API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"

# Language Pair Dictionary
MODEL_MAP = {
    ("english", "hindi"): "facebook/mbart-large-50-many-to-many-mmt",
    ("hindi", "english"): "facebook/mbart-large-50-many-to-many-mmt",
    ("english", "french"): "facebook/mbart-large-50-many-to-many-mmt",
    ("french", "english"): "facebook/mbart-large-50-many-to-many-mmt",
    ("english", "spanish"): "facebook/mbart-large-50-many-to-many-mmt",
    ("spanish", "english"): "facebook/mbart-large-50-many-to-many-mmt",
    ("english", "german"): "facebook/mbart-large-50-many-to-many-mmt",
    ("german", "english"): "facebook/mbart-large-50-many-to-many-mmt",
    ("english", "japanese"): "facebook/mbart-large-50-many-to-many-mmt",
    ("japanese", "english"): "facebook/mbart-large-50-many-to-many-mmt"
}

# Language Codes
LANG_CODES = {
    "English": "en_XX",
    "Hindi": "hi_IN",
    "French": "fr_XX",
    "Spanish": "es_XX",
    "German": "de_DE",
    "Japanese": "ja_XX"
}

PIVOT_LANGUAGE = "english"  # English as a bridge language

def perform_translation(text, src_lang, tgt_lang):
    """Calls Hugging Face API for translation"""
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": text,
        "parameters": {"src_lang": src_lang, "tgt_lang": tgt_lang}
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=300)

    if response.status_code == 200:
        return response.json()[0]["translation_text"]
    else:
        return f"❌ Translation failed: {response.json()}"

def translate_text(text, source_lang, target_lang):
    """Translates text directly or via English as a bridge"""
    source_lang = source_lang.lower()
    target_lang = target_lang.lower()

    model_name = MODEL_MAP.get((source_lang, target_lang))
    if model_name:
        return perform_translation(text, LANG_CODES[source_lang.capitalize()], LANG_CODES[target_lang.capitalize()])

    if source_lang != PIVOT_LANGUAGE and target_lang != PIVOT_LANGUAGE:
        pivot_text = perform_translation(text, LANG_CODES[source_lang.capitalize()], LANG_CODES[PIVOT_LANGUAGE.capitalize()])
        if not pivot_text:
            return None
        return perform_translation(pivot_text, LANG_CODES[PIVOT_LANGUAGE.capitalize()], LANG_CODES[target_lang.capitalize()])

    return "❌ Translation path not found."

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles form submission and redirects to result page"""
    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        translated_text = translate_text(text, source_lang, target_lang)

        return render_template("result.html", 
                               text=text, 
                               source_lang=source_lang, 
                               target_lang=target_lang, 
                               translated_text=translated_text)

    return render_template("index.html", lang_codes=LANG_CODES.keys())

if __name__ == "__main__":
    app.run(debug=True)
