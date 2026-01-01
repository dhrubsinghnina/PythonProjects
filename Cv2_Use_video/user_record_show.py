import cv2
import os
class UserCamera():
    def OpenCamera(self):
        # creating Camera object
        camera=cv2.VideoCapture(0)
        while True:
            # reading the video
            success,frame=camera.read()
            if not success:
                print("Webcam not opend:")
                break
            cv2.imshow("Camera open Only:",frame)
            if cv2.waitKey(1) & 0XFF==ord('q'):
                print("Camera closed:")
                break
        camera.release()
        cv2.destroyAllWindows()
    def RecordCamera(self):
        # creating Camera object
        camera=cv2.VideoCapture(0)
        # makig width and height:
        frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        codec=cv2.VideoWriter_fourcc(*'XVID') #type:ignore
        name=input("enter file name :")
        # creating recoder object:
        recoder=cv2.VideoWriter(f"Cv2_Use_video/user_video/{name}.avi",codec,20,(frame_width,frame_height))
        while True:
            # reading the video
            success,frame=camera.read()
            if not success:
                print("Webcam not opend:")
                break
            recoder.write(frame)
            cv2.imshow("Your video",frame)
            if cv2.waitKey(1) & 0XFF==ord('q'):
                print("Quiting..")
                break
        camera.release()
        cv2.destroyAllWindows()
    def ShowVideo(self):
        path=input('Enter file path:')
        video=cv2.VideoCapture(f"Cv2_Use_video/user_video/{path}.avi")
        while True:
            success,frame=video.read()
            if not success:
                print("Not opend")
                break
            cv2.imshow("Opend video:",frame)
            if cv2.waitKey(50) & 0XFF==ord('q'):
                print("Quiting..")
                break
        video.release()
        cv2.destroyAllWindows()
    def DeleteVideo(self):
        name=input("Enter file name:")
        path = f"Cv2_Use_video/user_video/{name}.avi"
        if os.path.exists(path):
            os.remove(path)
            print(f"Video '{name}.avi' deleted successfully.")
        else:
            print("File not found. Please check the file name.")
            
UseCam=UserCamera()

while True:
    i=int(input("""
                Enter 1 to open camera only:
                Enter 2 to record video:
                Enter 3 to show video:
                Enter 4 to delete video:
                """))
    if i==1:
        UseCam.OpenCamera()
    elif i==2:
        UseCam.RecordCamera()
    elif i==3:
        UseCam.ShowVideo()
    elif i==4:
        UseCam.DeleteVideo()
    elif i==-1:
        print("Thank you")
        break
    else:
        i=int(input("Invalid entry try again:"))