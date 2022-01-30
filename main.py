from statistics import mode
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb",
                       title="Choose a file", filetypes=[
                           ("image", ".png"),
                           ("image", ".jpg"),
                           ("image", ".jpeg")])
    if file:
        read_img = Image.open(file)
        read_img = ImageTk.PhotoImage(read_img)
        read_img_label = tk.Label(image=read_img)
        read_img_label.image = read_img
        read_img_label.grid(column=1, row=3)


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open("tomato.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


# Instructions
instructions = tk.Label(
    root, text="Select a Photo file on your coputer to extract and add water mark to it", font="Ubuntu")
instructions.grid(columnspan=3, column=0, row=1)

# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       font="Ubuntu", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
