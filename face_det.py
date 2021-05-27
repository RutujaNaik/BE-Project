
# FACE DETECTION and DEMARCATION 

# --------------------- VIDEO -----------------------------

import cv2
import numpy as np
import dlib


cap = cv2.VideoCapture(0)  
  
# Detect the coordinates
detector = dlib.get_frontal_face_detector()
  
  
# Capture frames continuously
while True:
  
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
  
    # RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
  
    # Iterator to count faces
    i = 0
    for face in faces:
  
        # Get the coordinates of faces
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
  
        # Increment iterator for each face in faces
        i = i+1
  
        # Display the box and faces
        #cv2.putText(frame, 'face num'+str(i), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)
        if i > 1:
            print("More than one face detected")
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
  
    # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
  
# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()

"""

# ----------------- STATIC IMAGES ----------------------

    
def face_det(path):
    # load the photograph
    pixels = cv2.imread(path)
    
    # load the pre-trained model
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels)
    
    print(len(bboxes))
    
    # print bounding box for each detected face
    for box in bboxes:
    	print(box)
        # extract
    	x, y, width, height = box
    	x2, y2 = x + width, y + height
    	# draw a rectangle over the pixels
    	cv2.rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
    
    # show the image
    cv2.imshow('face detection', pixels)

    # keep the window open until we press a key
    cv2.waitKey(0)
    
    # close the window
    cv2.destroyAllWindows() 
    #pad(box) 
    
#def pad(face_dims):
#    print(face_dims) 
    
#face_det("C:\\Users\harsh\\Desktop\\projBE\\frnds.jpg")
""" 

