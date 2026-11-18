
import joblib
import numpy as np
from preprocess import process_review
from flask import Flask,request, jsonify

app=Flask(__name__)

model=joblib.load('model.joblib') # loading the saved model
vectorizer=joblib.load('vectorizer.joblib') # loading the saved TF-IDF vectorizer

@app.route("/predict",methods=["POST"]) # whenever user posts data to predict call this func
def predict():
    data=request.get_json() #read the incoming json data

    review=data['reviews'] # extract the review from dict

    process_rev=process_review(review) # preprocess the review posted

    process_rev=vectorizer.transform([process_rev]) #extract features from the review

    prediction =model.predict(process_rev)# predict the sentiment

    return jsonify({"prediction":"positive" if prediction[0] == "1" else "negative"}) #output the sentiment.jsonify is used to convert python dict to json obj
@app.route("/health",methods=['GET']) #used to check if the server is running it ll output {"status";"ok} if server is running

def health():
    return josonify({"status":"ok"})

if __name__ == "__main__":
    #app.run(debug=true,host=0.0.0.",port=50000)host:0.0.0.0 means any compu can connect to this host
    import os
    app.run(host="127.0.0.1",port=int(os.environ.get("PORT",5000)))