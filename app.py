from pyexpat import model
import sklearn
import numpy as np
from flask import Flask, render_template, request
from model import load

app = Flask(__name__)
app.static_folder = 'static'
model, scaler = load()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predictions")
def predictions():
    return render_template("predictions.html")

@app.route("/car")
def car():
    return render_template("car.html")

@app.route("/visualisasi")
def visualisasi():
    return render_template("visualisasi.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/predict', methods=['POST'])
def predict():
    Merek = int(request.form['Merk'])
    Model = int(request.form['MDl'])
    Varian = int(request.form['VAR'])
    Tahun = int(request.form['THN'])
    Jarak_tempuh = int(request.form['JT'])
    
    data_baru = np.array([[Merek, Model, Varian, Tahun, Jarak_tempuh]])

    Prediction = model.predict(data_baru)
    Prediction = Prediction * 100000000
    Prediction = int(Prediction)
    Prediction = round(Prediction)
    Prediction_formatted = "{:,.2f}".format(Prediction)

    # Hasil prediksi
    print(f'Harga mobil bekas tersebut diprediksi sebesar Rp {Prediction_formatted}')

    return render_template('predictions.html', prediction=Prediction_formatted, data=data_baru)

if __name__ == "__main__":
    app.run(debug=True)