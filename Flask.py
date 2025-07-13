from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from google import genai
from google.genai import types

# API-ключ можно вставить напрямую
genai.configure(api_key="AIzaSyDQagUVc-vwnGBobU343KXoT4lPonDf3YE")

app = Flask(__name__)
CORS(app)

@app.route("/gemini", methods=["POST"])
def gemini():
    prompt = request.json.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Empty prompt"}), 400

    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run()
