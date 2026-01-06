import cv2
class CannyAndThres():
    def Open(self):
        camera=cv2.VideoCapture(0)
        while True:
            ret,frame=camera.read()
            if not ret:
                print("Camera can not not capture: ")
                break
            cv2.imshow("Camera open:",frame)
            if cv2.waitKey(1) & 0XFF==ord('q'):
                print("Quiting..")
                break
        camera.release()
        cv2.destroyAllWindows()
    def canny(self):
        camera=cv2.VideoCapture(0)
        while True:
            ret,frame=camera.read()
            if not ret:
                print("Camera can not not capture: ")
                break    
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            edgeFrame=cv2.Canny(gray,100,150)
            cv2.imshow("edge image=",edgeFrame)
            if cv2.waitKey(1) & 0XFF==ord('q'):
                print("Quiting..")
                break
        camera.release()
        cv2.destroyAllWindows()
    def thresh(self):
        camera=cv2.VideoCapture(0)
        while True:
            ret,frame=camera.read()
            if not ret:
                print("Camera can not not capture: ")
                break
       
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            _,threhFrame=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
            cv2.imshow("edge image=",threhFrame)
            if cv2.waitKey(1) & 0XFF==ord('q'):
                print("Quiting..")
                break
        camera.release()
        cv2.destroyAllWindows()
CannThresh=CannyAndThres()  
while True:
    i=int(input("""
                Enter 1 to open camera:
                Enter 2 to open cnnny:
                Enter 3 ton open thresh:
                Enter -1 to eccape:"""))
    if i==1:
        CannThresh.Open()
    elif i==2:
        CannThresh.canny()
    elif i==3:
        CannThresh.thresh()
    elif i==-1:
        break
    else:
        print("Invalid entry:\nTry again:")
    