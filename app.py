from flask import Flask, jsonify, render_template, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@cross_origin
@app.route('/',methods=['GET'])
def home():
    file = open("./spam-ham.txt","r")
    spam= file.read(3)
    ham= file.read(3)
    return jsonify(cantidad=[{"Spam": str(spam),"Ham":str(ham)}])

@cross_origin
@app.route('/image',methods=['GET'])
def image():
    return send_file('./Correos.jpg',attachment_filename='Correos.jpg')

@cross_origin
@app.route('/prediction',methods=['GET'])
def prediction():
    file= open('./prediction.txt',"r")
    prediction = file.read()
    return jsonify(pre=[{"Prediction": str(prediction)}])

@cross_origin
@app.route('/accuracy',methods=['GET'])
def accuracy():
    file= open('./accuracy.txt',"r")
    accuracy = file.read()
    return jsonify(accu=[{"Accuracy": str(accuracy)}])

if __name__ == '__main__':
    app.run(port=5000)