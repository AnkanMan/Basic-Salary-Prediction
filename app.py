from flask import *
import pickle
import numpy as np

app = Flask(__name__)
# model loading
model = pickle.load(open('SalaryPredicter.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    np_features = [np.array(features)]
    pred = model.predict(np_features)
    output = round(pred[0],2)
    pred_text = "Your Predicted Salary is Rs {}".format(output-10000)
    return render_template('index.html',prediction = pred_text)


if __name__ == '__main__':
    app.run(debug = True)