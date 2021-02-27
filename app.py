from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Duration= int(request.form['Duration'])
        Heart_Rate = int(request.form['Heart_Rate'])
        Age= int(request.form['Age'])
        Weight = int(request.form['Weight'])
        data =[Duration,Heart_Rate,Age,Weight]
        data= np.array(data)
        data =data.reshape(1,-1)
        my_prediction = model.predict(data)
        output=my_prediction
        if output>3500:
            return render_template('index.html',prediction_texts="Exceeded the calories burn {}".format(output*10))
        else:
            return render_template('index.html',prediction_text="Calories burned  {}".format(output*10))
    else:
        return render_template('index.html')
        
     
if __name__=="__main__":
    app.run(debug=True)
