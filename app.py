from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@cross_origin
@app.route('/',methods=['GET'])
def home():
    file = open("./entrenamiento.txt","r")
    spam= file.read(3)
    ham= file.read(3)
    return jsonify(correos=[{"spam": str(spam),"ham":str(ham)}])

@cross_origin
@app.route('/imagen',methods=['GET'])
def image():
    return send_file('./Correos.jpg',attachment_filename='Correos.jpg')

@cross_origin
@app.route('/prediccion',methods=['GET'])
def prediction():
    file= open('./prediccion.txt',"r")
    prediction = file.read()
    return jsonify(prediccion=[{"Prediccion": str(prediction)}])

@cross_origin
@app.route('/porcentaje',methods=['GET'])
def accuracy():
    file= open('./accuracy.txt',"r")
    accuracy = file.read()
    return jsonify(porcentaje=[{"porcentaje": str(accuracy)}])

if __name__ == '__main__':
    app.run(port=5000)