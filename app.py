from flask import Flask, render_template
from flask import Flask
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

model_file = open('model_uas1.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

 int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text='Your predicted annual Healthcare Expense is $ {}'.format(output))
    
@app.route('/results',methods=['POST'])
def results():
        disaster1=pd.read_csv('glcm_disaster1.csv')(force=True)
    prediction = model.file([np.array(list(data.values()))])

    output = prediction[0]
    return model_file(output)

if __name__ == "__main__":
    app.run (debug=True)