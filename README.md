# Car Rear Detector


This is repo is a submission for AI4AV Assignment 7 Spring 2022, WPI, professor Morato.



### Problem statement

Object detection and localisation for rear view of car from dash cam.

Autonomous driving is only a few years away from realisation. A good object detection and localisation model is essential for safety requirements. This assignment is executed by a YOLO model pretrained on VOC dataset.



### Methodology 

I installed darknet framework for the execution of this task / assignment. 

This decision was taken because it makes little sense to re-invent the wheel and YOLO because the model is reobust and has delivered good results.


### Dataset 

The berkley driving dataset 10k comprising of 10,000 images was installed for this purposes since the initial link provided in the pdf wasn't working.


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

![]('https://raw.githubusercontent.com/deveshdatwani/car-rear-detector/main/assets/sampledetect.png')
