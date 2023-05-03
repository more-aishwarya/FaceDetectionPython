# FaceDetectionPython


OpenCV is a computer vision library that supports programming languages like Python, C++, and Java.
The package was initially created by Intel in 1999 and was later made open-source and released to the public.
OpenCV allows developers and non-mathematicians to build computer vision applications easily without having to code them from scratch. The library has over 2,500 algorithms that allow users to perform tasks like face recognition and object detection.
Face detection involves identifying a person’s face in an image or video. This is done by analyzing the visual input to determine whether a person’s facial features are present.
Since human faces are so diverse, face detection models typically need to be trained on large amounts of input data for them to be accurate. 
The library employs a machine learning approach called Haar cascade to identify objects in visual data. 
To install the OpenCV library, we need to run following command :
         pip install opencv-python


The Haar Cascade classifier is built into OpenCV and has already been trained on a large dataset of human faces. We just need to load the classifier from the library and use it to perform face detection on an input image. We are using a file called haarcascade_frontalface_default.xml. This classifier is designed specifically for detecting frontal faces in visual input. 
OpenCV also provides other pre-trained models to detect different objects within an image - such as a person’s eyes, smile, upper body, and even a vehicle’s license plate. You can learn more about the different classifiers built into OpenCV by examining the library’s
We have downloaded haarcascade_frontalface_default.xml file from following source :
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml


