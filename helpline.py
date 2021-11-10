#GEt help

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("HELPLINE")

def order():

    tmsg.showinfo("Request Received!", f"We have received your  {var.get()}. WE will reach you soon")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "How can we help?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Call ", padx=14, variable=var, value="Call Request").pack(anchor="w")
radio = Radiobutton(root, text="Chat ", padx=14, variable=var, value="Chat Request").pack(anchor="w")
radio = Radiobutton(root, text="Mail", padx=14, variable=var, value="Mail Request").pack(anchor="w")
radio = Radiobutton(root, text="Other help info", padx=14, variable=var, value="Request CALL US AT 199 or Mail Us At savelife@gmail.com").pack(anchor="w")

Button(text="Get Help Now", fg="#ffffff", bg="#3F3351", command=order).pack()
root.mainloop()