from cnnClassifier.pipeline.prediction import prediction

test_image_path='artifacts\data_ingestion\Chest-CT-Scan-data\normal\3.png'

predictor=prediction(test_image_path)

result=predictor.predict()

print(result)