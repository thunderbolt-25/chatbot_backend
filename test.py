import google.generativeai as genai

# Initialize the Gemini API client with the key
genai.configure(api_key="GEMINI_API_KEY")

def list_available_models():
    try:
        models = list(genai.list_models())  # Convert the generator to a list
        print(f"Available models: {models}")
        return models
    except Exception as e:
        print(f"⚠️ Error listing models: {e}")
        return None

models = list_available_models()  # Run this to see the available models
