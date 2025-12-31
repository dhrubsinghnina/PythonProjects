import cv2

x=int(input("Enter 1 to load an image else -1:"))
while x==1:
    # taking user input image path:
    img_path=input("Enter image path :")
    # loading image from path:
    image=cv2.imread(img_path)
    if image is not None:
        print("Image loaded successfullt:")
        # resizing the image
        width=int(input("Enter width of the image :"))
        height=int(input("Enter height of the image :"))
        resized_image=cv2.resize(image,(width,height))
        # user decied of color of gray:
        y=int(input("Enter 1 for colerd and 2 for gray :"))
        if y==1:
            change_image=resized_image
        elif y==2:
            # gray scale conversion:
            change_image=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
        i=int(input("Enter 1 for save or Enter 2 for show:"))
        while i!=-1:
            if i==1:
                save_name=input("Enter saving file name of the image:")
                Path=f"C:/Users/dhrub/OneDrive/Desktop/gitupdate/PythonProjects/Cv2_colored_gray/saved_images/{save_name}"
                cv2.imwrite(Path,change_image)
            elif i==2:
                show_name=input("Enter showing name :")
                cv2.imshow(show_name,change_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Invalid entry:")
            i=int(input("Enter 1 for save or Enter 2 for show -1 to exit this image:"))
    else:
        print("Error:Image is not loaded:")
    x=int(input("Enter 1 to load an image else -1:"))
else:
    print("Thank you sir:")