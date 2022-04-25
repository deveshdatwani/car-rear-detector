def cal_IOU(coord_1, coord_2):

	x_right = coord1[0]
	x_left = coord2[0]
	y_right = coord2[1]
	y_left = coord2[1]

	intersection_area = (x_right - x_left) * (y_bottom - y_top)

	return intersection_area

import os

images = os.listdir('10k/val')
with open('detections.txt') as file:
	data = file.read()

with open('annotations.json') as annot:
	data = json.loads(annot.read()))

average_IOU = []

for image in data:
	for i in data:
		if i == image['name']:
			average_IOU.append(cal_IOU(image, i))
		else:
			pass

print(average_IOU/len(average_IOU))

