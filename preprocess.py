import json

with open('./trainning.json') as json_file:
	data = json.load(json_file)
print(len(data['annotations']))
print(data.keys())
print(data['annotations'][0])
# val = {}
# val['info'] = data['info']
# val['images'] = []
# val['annotations'] = []
# val['categories'] = data['categories']
# # val['annotations'][:500] = data[:500]
# for i in range(0,500):
# 	val['annotations'].append(data['annotations'][i])
# 	data['annotations'].pop(i)
# 	val['images'].append(data['images'][i])
# 	data['images'].pop(i)
# 	pass
# print(val['annotations'][0])
# print(val['images'][0])
# print(val.keys())
# with open('validation.json', 'w') as fp:
#     json.dump(val, fp)
# with open('trainning.json', 'w') as fp:
#     json.dump(data, fp)