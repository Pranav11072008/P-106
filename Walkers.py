import cv2

gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    
    bodies = body_cascade.detectMultiScale(gray)
    # Extract bounding boxes for any bodies identified
     for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow(frame) 
      

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
