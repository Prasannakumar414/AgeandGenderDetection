from tkinter import *
from PIL import Image, ImageTk
import cv2

MainWindow = Tk()
MainWindow.title('Age and Gender Detection')
MainWindow.geometry("1000x1000")

Heading=Label(MainWindow, text="Age and Gender Detection",font=('Helvetica bold',50))
Heading.place(x="550",y="100")#co-ordinates of Heading


label =Label(MainWindow)
label.place(x="600",y="200")#co-ordinates of video displayed

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap= cv2.VideoCapture(0)

def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   faces = face_cascade.detectMultiScale(cv2image, 1.1, 4)
   for (x, y, w, h) in faces:
        cv2.rectangle(cv2image, (x, y), (x+w, y+h), (255, 0, 0), 2)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)
quitButton = Button(MainWindow, text='quit', width=25, command=MainWindow.destroy)
quitButton.place(x="800",y="900")#co-ordinates of the quit-button
MainWindow.attributes('-fullscreen', True)
show_frames()
MainWindow.mainloop()

