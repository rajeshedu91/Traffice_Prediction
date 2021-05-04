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
        area = request.form['area'].lower()
        time = request.form['time'].lower()
        day = request.form['day'].lower()
        # text = request.form['text'].lower()
        text = area + ' ' + day + ' ' + 'at ' +time
        print(text)
        processed_text = [text]
        output = loaded_model.predict(processed_text)
        print(output)
        return render_template("index.html", result=output, text = text)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)