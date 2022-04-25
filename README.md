# Car Rear Detector


This is repo is a submission for AI4AV Assignment 7 Spring 2022, WPI, professor Morato.



### Problem statement

Object detection and localisation for rear view of car from dash cam.

Autonomous driving is only a few years away from realisation. A good object detection and localisation model is essential for safety requirements. This assignment is executed by a YOLO model pretrained on VOC dataset.



### Methodology 

I installed darknet framework for the execution of this task / assignment. 

This decision was taken because it makes little sense to re-invent the wheel and YOLO because the model is reobust and has delivered good results.


### Dataset 

The berkley Deep Drive dataset 10k comprising of 10,000 images was installed for this purposes since the initial link provided in the pdf wasn't working.


### Loading the YOLO model

Once the darknet repo has been cloned to the system, the weights can be loaded by the command

``` 
./darknet -nogpu imagenet test cfg/alexnet.cfg alexnet.weights

```

The nogpu argument tells the framework that my system has no GPU. 


### Initial run

First I tried to run the model on a sample image from the dataset by using the command 


``` 
./darknet detect cfg/yolov3.cfg yolov3.weights data/samplescene.jpg
```

where I renamed an image to 'samplescene.jpg' 

The results were as follows

![sample detect](https://raw.githubusercontent.com/deveshdatwani/car-rear-detector/main/assets/sampledetect.png)

### Training

For training, I trained YOLO model only on 1000 images from val 10k dataset since my system cannot handle more than that. 


The config files for annotations need to be in .yaml format. For this I created a script in data/ folder. 

This structures the bounded boxes annotations .json file into .yaml a file which is required by YOLO model. 

The training can be started witht the command

``` 
!python train.py --img 640 --cfg yolov5s.yaml --hyp hyp.scratch.yaml --batch 32 --epochs 100 --data data.yaml --weights yolov5s.pt --workers 24 --name yolo_det
```


### Testing accuracy 

To test accuracy, 

```
./darknet detector 10k/val cfg/obj.data cfg/yolov3.cfg yolov3.weights < images_files.txt
```

The above command detects every image in the folder 10k/val and outputs the predictions stores in file path in images_files.txt.

It can be outputted to a new txt file which will be used to carry out detection accuracy

For this, I wrote a script to calculate IoU.

```
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

```


### RESULT

Average IoU was 0.88 on the 1000 val dataset





## NOTE

The .json and .txt files were above 100mb, hence I didn't add them to the repo
