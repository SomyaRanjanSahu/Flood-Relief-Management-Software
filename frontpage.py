#FRONTPAGE
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)

root.geometry("1920x1080")
root.title("Flood Management")




f1 = Frame(root, borderwidth=8, bg="#697003", )
f1.pack(side=BOTTOM, fill="x")


l = Label(f1, text="SAVE LIFE",height=3,width=1500, font="Helvetica 30 bold", bg="#EAEF64", pady=0)
l.pack()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM)

def CS():
    print("You will be directed to the Current stats soon")

def D():
    print("Donation window will appear ")
def GH():
    print("Help is on the way")

def SM():
    print("Saftey Measures will appear soon")
 

redbutton = Button(frame, text="CURRENT STATS",font="comicsansms 8 bold",fg="white", bg="#697003",height = 5,
          width = 55,command=CS)
redbutton.pack( side = LEFT)
          

greenbutton = Button(frame, text="DONATIONS",  font="comicsansms 8 bold",fg="white", bg="#697003",height = 5,
          width = 55,command=D)
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="GET HELP",font="comicsansms 8 bold",  fg="white", bg="#697003",height = 5,
          width = 55,command=GH)
bluebutton.pack( side = LEFT )

blackbutton = Button(frame, text="SAFTEY MEASURES", font="comicsansms 8 bold", fg="white", bg="#697003",height = 5,
          width = 55,command=SM)
blackbutton.pack( side = LEFT)
label = Label(image=photo)
label.pack()

root.mainloop()
