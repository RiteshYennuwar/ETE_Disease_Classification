from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.utils.common import decodeImage
from src.pipeline.predection import PredectionPipeline

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class APP:
    def __init__(self) -> None:
        self.filename = 'InputImage.jpg'
        self.classifier = PredectionPipeline(self.filename)

clApp = APP()

os.system('dvc repro')

@app.route('/', methods =['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000)
    # app.run(host='0.0.0.0', port = 80)