from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


def display_logo(url, row, column):
    img = Image.open(url)
    # resize image
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img)
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2,
                   sticky=NW, padx=20, pady=40)


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb",
                       title="Choose a file", filetypes=[
                           ("image", ".png"),
                           ("image", ".jpg"),
                           ("image", ".jpeg")])
    if file:
        read_img = Image.open(file)
        read_img = read_img.resize(
            (int(read_img.size[0]/5), int(read_img.size[1]/5)))
        read_img = ImageTk.PhotoImage(read_img)
        read_img_label = Label(image=read_img)
        read_img_label.image = read_img
        read_img_label.grid(column=0, row=2, sticky=SW, padx=25, pady=25)
        browse_text.set("Browse")


root = Tk()

header = Frame(root, width=800, height=175)
header.grid(columnspan=3, rowspan=2, row=0)

# main content area - image extraction
main_content = Frame(root, width=800, height=250)
main_content.grid(columnspan=3, rowspan=2, row=2)

# logo
display_logo('tomato.png', 0, 0)


# Instructions
instructions = Label(root, text="Select a image file",
                     font=("Ubuntu", 10))
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

# Browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda: open_file(),
                    font="Ubuntu", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)


root.mainloop()
