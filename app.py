import json
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API Key for Gemini
GEMINI_API_KEY = "AIzaSyAZG8hH9B2yzk2-nlEJcUN56CAzmA1lhRg"
genai.configure(api_key=GEMINI_API_KEY)

# Load FAQ data
try:
    with open("faq_data.json", "r", encoding="utf-8") as file:
        faq_data = json.load(file)
except FileNotFoundError:
    print("⚠️ Error: 'faq_data.json' not found. Make sure the file is in the project folder.")
    faq_data = []

# Search for FAQ answer based on user query
def find_faq_answer(query):
    for item in faq_data:
        if query.lower() in item["question"].lower():
            return item["answer"]
    return None  

# List available models in Gemini
def list_available_models():
    try:
        # Use the method to list available models
        models = genai.list_models()
        print("🔹 Available Models:")
        for model in models:
            print(f"- {model.name}")
        return models
    except Exception as e:
        print(f"⚠️ Error listing models: {e}")
        return []

# Fetch response from Gemini AI
def fetch_gemini_response(query):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use the correct model name
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        print(f"⚠️ Gemini API Error: {e}")
        return "⚠️ Gemini AI service is currently unavailable. Please try again later."
    
  


# Fetch response based on user query (first check FAQs, then Gemini)
def fetch_response(query):
    faq_answer = find_faq_answer(query)
    if faq_answer:
        return faq_answer  # Return FAQ answer if found
    
    return fetch_gemini_response(query)  # Otherwise, use Gemini AI

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("query")
        if not user_input:
            return jsonify({"response": "⚠️ Invalid request. Please send a valid query."}), 400

        ai_response = fetch_response(user_input)
        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"⚠️ Internal Server Error: {e}")
        return jsonify({"response": "⚠️ An error occurred on the server. Please try again."}), 500

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
