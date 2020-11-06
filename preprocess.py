import json

with open('../traffic_train/train_traffic_sign_dataset.json') as json_file:
	data = json.load(json_file)
print(len(data['annotations']))
print(data['annotations'][0])