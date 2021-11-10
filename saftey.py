#Saftey mesures

from tkinter import *
root = Tk()
root.geometry("1920x1080")
root.title("Saftey Measures")

f2 = Frame(root, borderwidth=8, bg="black", )
f2.pack(side=TOP, fill="x")

l = Label(f2, text="SAFTEY MEASURES", font="Helvetica 60 bold", fg="red", bg="#D5D5D5",pady=22)
l.pack()


title_label = Label(text =''' Staying Safe is Most Important

The five safety rules you should practice during a flood listed here are meant to help you stay safe during this type of natural disaster. 
Your first priority should always be getting yourself and your loved ones to a safe location, away from the flooded area.
While it may be tempting to try to rescue cherished possessions before fleeing, this would be a mistake. 
You can always replace "stuff," but a life can never be recovered after the flood waters subside
1. Stay informed about flooding conditions in your area
2. Don't try to walk through a flooded area
3. Avoid flooded areas if you are in a vehicle
4. A stalled car should be abandoned immediately
5. Evacuate a flooded area immediately if instructed to do so.

CALL US AT 198 FOR EMERGENCY

''', bg ="black", fg="white", padx=13, pady=250, font="comicsansms 16 bold", borderwidth=9, relief=SUNKEN)



title_label.pack(side=BOTTOM, fill=X, padx=34, pady=34)


root.mainloop()