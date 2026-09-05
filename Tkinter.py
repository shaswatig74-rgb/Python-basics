from tkinter import Tk,  Label, Button, Frame, messagebox, Entry
from PIL import Image, ImageTk

# intialize tkinter
windows = Tk()

windows.geometry("400x300")
windows.title("My Tkinter App")

frame = Frame(windows, bg = "deepskyblue", padx = 10, pady = 10)
frame.pack(fill="both", expand = True)

# widgets

username_label = Label(frame, text = "Enter Username", padx = 5, pady = 5, bg = "deepskyblue")
username_label.grid(row=0, column=0)

img_file = Image.open("OIP.webp")
img_file = img_file.resize((250, 250))
photo = ImageTk.PhotoImage(img_file)
pic = Label(frame, image=photo)
pic.grid(row=1, column=1)

def show_message():
     messagebox.showwarning("Attention please!", "Virus Attack")


btn = Button(frame, text="Click", bg="pink",command=show_message)
btn.grid(row=1, column=0, padx=5, pady=5)

username_input = Entry(frame) 
username_input.grid(row=0, column=1, padx = 5, pady = 5)


# keep the window open till we close it manually

windows.mainloop()


