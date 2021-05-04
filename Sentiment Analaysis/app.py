from flask import Flask, render_template, request
import os
import joblib

# Initialize flask app
app = Flask(__name__)
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)

# @app.route('/')
# def index():
#   return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        text = request.form['text'].lower()
        processed_text = [text]
        output = loaded_model.predict(processed_text)
        print(output)
        return render_template("index.html", result=output)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)