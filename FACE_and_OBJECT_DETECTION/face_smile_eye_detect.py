import cv2 

face_cascade=cv2.CascadeClassifier("FACE_and_OBJECT_DETECTION/haarcascade_frontalface_alt.xml")
eye_cascade=cv2.CascadeClassifier("FACE_and_OBJECT_DETECTION/haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("FACE_and_OBJECT_DETECTION/haarcascade_smile.xml")

camera=cv2.VideoCapture(0)

while True:
    ret,frame=camera.read() # true/false,one frame
    if not ret:
        print("Could not read properly:")
        break
    # making gray
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray_frame,1.1,5) #image,scaler factor,min neighbour
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # croping of face:
        roi_gray  = gray_frame[y:y+h, x:x+w] # for Harr cascade
        # roi_color = frame[y:y+h, x:x+w] # for draw on frame

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        if len(eyes)>0:
            cv2.putText(frame,"eye detected",(x+30,y-40),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.2, 20)
        if len(smiles)>0:
            cv2.putText(frame,"smile detected",(x+30,y-20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

    
    cv2.imshow("Webcam_face:",frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        print("Quiting")
        break
camera.release()
cv2.destroyAllWindows()
    