import os
from cnnClassifier.pipeline.prediction import prediction
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS,cross_origin
from cnnClassifier.utils.common import decodeImage

os.putenv('LANG','EN_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')


app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=prediction(self.filename)
    

@app.route("/",method=['GET'])
@cross_origin
def home():
    return render_template('templates\index.html')

@app.route("/train",method=['GET','PUT'])
@cross_origin
def trainRoute():
    os.system('dvc repro')
    return 'Training completed'

@app.route("/predict",method=['GET'])
@cross_origin
def predict():
    image=request.json(['image'])
    decodeImage(image,clApp.filename)
    result=clApp.classifier.predict()
    return jsonify(result)


if __name__=='__main__':
    clApp=ClientApp()
    app.run(host='0.0.0.0',port=8080)