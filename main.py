
import cv2
import os
#Load image for face detection

img = cv2.imread('image3.jpg')

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Check if the face detection classifier file exists and is not empty
if not os.path.isfile('haarcascade_frontalface_default.xml'):
    print("Error: face detection classifier file does not exist or is empty")
else:
    # Load the image
    img = cv2.imread('image3.jpg')

    # Check if the image file exists and is not empty
    if img is None:
        print("Error: image file does not exist or is empty")
    else:
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the image with detected faces
        cv2.imshow('Detected Faces', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()