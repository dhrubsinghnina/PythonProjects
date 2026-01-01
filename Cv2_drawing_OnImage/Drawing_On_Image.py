import cv2
class ImageDrawing():
    def __init__(self, image):
        self.image = image   # public to all methods
    def drawLine(self):
        pt=(input("Enter pt1= X1,y1:")).split(",")
        PT1 = tuple(map(int, pt))
        pt=(input("Enter pt1= X2,y2:")).split(",")
        PT2=tuple(map(int, pt))
        color=(input("Enter Blue,Green,Red:")).split(",")
        color=[int(x) for x in color]
        thickness=int(input("Enter thickness:"))
        cv2.line(self.image,PT1,PT2,color,thickness)
    def drawRectangle(self):
        pt=(input("Enter pt1(top left corner of rectangle)= X1,y1:")).split(",")
        PT1 = tuple(map(int, pt))
        pt=(input("Enter pt1(top roght corner of the rectangle)= X2,y2:")).split(",")
        PT2=tuple(map(int, pt))
        color=(input("Enter Blue,Green,Red:")).split(",")
        color=[int(x) for x in color]
        thickness=int(input("Enter thickness:"))
        cv2.rectangle(self.image,PT1,PT2,color,thickness)
    def drawCircle(self):
        center=(input("Enter Centor of th circle (x,y):")).split(",")
        Center=tuple(map(int,center))
        radius=int(input("Enter radius of the circle:"))
        color=(input("Enter Blue,Green,Red:")).split(",")
        color=[int(x) for x in color]
        thickness=int(input("Enter thickness:"))
        cv2.circle(self.image,Center,radius,color,thickness)
    def addText(self):
        text=input("Enter text:")
        color=(input("Enter Blue,Green,Red:")).split(",")
        color=[int(x) for x in color]
        thickness=int(input("Enter thickness:"))
        pt=input("Enter buttom left of the text(X,Y):").split(",")
        org=tuple(map(int,pt))
        fontSize=int(input("Enter font size:"))
        cv2.putText(self.image,text,org,cv2.FONT_HERSHEY_SIMPLEX,fontSize,color,thickness)
    def showImage(self):
        cv2.imshow("Drawn image",self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def saveImage(self):
        name=input("Enter name of the file:")
        cv2.imwrite(f"C:/Users/dhrub/OneDrive/Desktop/gitupdate/PythonProjects/Cv2_drawing_OnImage/DrawnImages/{name}",self.image)
x=int(input("Enter 1 for read image:"))
while x==1:
    path=input("Enter path of the image :")
    image=cv2.imread(path)
    if image is not None:
        print("Image loaded succesfully:")
        print("-----Resize the image-----")
        width=int(input("Enter width:"))
        height=int(input("Enter height:"))
        image=cv2.resize(image,(width,height))
        original=image.copy()
        # creating object og the class:
        hitImage=ImageDrawing(image)
        i=int(input("""
            Enter 1 for draw a line:
            Enter 2 for draw a rectangle:
            Enter 3 for draw a circle:
            Enter 4 to add texk:
            Enter 5 to show:
            Enter 6 to save:
            Enter -1 to exit this image:
            Enter choice:"""))
        while i!=-1:
            if i==1:
                hitImage.drawLine()
            elif i==2:
                hitImage.drawRectangle()
            elif i==3:
                hitImage.drawCircle()
            elif i==4:
                hitImage.addText()
            elif i==5:
                j=int(input("Enter 1 to show original:else 2 to show drawn:"))
                if j==1:
                    cv2.imshow("Original",original)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                elif j==2:  
                    hitImage.showImage()
                else:
                    print("Invalid entry:")
            elif i==6:
                hitImage.saveImage()
            else:
                i=int(input("Invlid entry try again:"))
            i=int(input("try again:"))
    else:
        print("Error:Imgae is not loaded:")    
    x=int(input("Enter 1 to read new image else -1:"))
else:
    print("Thank you sir:")