
import joblib
import numpy as np
from preprocess import process_review
from flask import Flask, request, jsonify

app = Flask(__name__)

# Loading saved model and vectorizer
model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        review = data['reviews']

        process_rev = process_review(review)

        process_rev = vectorizer.transform([process_rev])

        prediction = model.predict(process_rev)

        sentiment = "positive" if str(prediction[0]) == "1" else "negative"

        return jsonify({"prediction": sentiment})

    except Exception as e:
        print("Prediction Error:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
