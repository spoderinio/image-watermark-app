from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
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
    global read_img_label, read_img, resized_image
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
        resized_image = ImageTk.PhotoImage(read_img)
        read_img_label = Label(image=resized_image)
        read_img_label.image = resized_image
        read_img_label.grid(column=0, row=2, rowspan=3,
                            sticky=SW, padx=25, pady=25)
        browse_text.set("Browse")
        return read_img


def add_text():
    # Define font
    text_font = ImageFont.load_default()
    # get text to add to image
    text_to_add = my_entry.get()

    # Edit the Image
    edit_image = ImageDraw.Draw(read_img)
    edit_image.text((700, 600), text_to_add, ("white"), font=text_font)

    # Save the Image
    read_img.save("image2.png")

    # Clear the entry box
    my_entry.delete(0, END)
    my_entry.insert(0, "Saving File...")

    # Wait a few seconds and then show image
    read_img_label.after(2000, show_pic)


def show_pic():
    global image2
    # SHow new Image
    image2 = PhotoImage(file="image2.png")
    read_img_label.config(image=image2)

    # Clear the entry box
    my_entry.delete(0, END)


root = Tk()

header = Frame(root, width=800, height=175)
header.grid(columnspan=3, rowspan=2, row=0)

# main content area - image extraction
main_content = Frame(root, width=800, height=250)
main_content.grid(columnspan=3, rowspan=3, row=2)

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

# Entry text

my_entry = Entry(root, font=("Ubuntu", 24))
my_entry.grid(column=1, row=2, sticky=SW)

# ADD Button
my_button = Button(root, text="Add text to Image",
                   command=add_text, font=("Ubuntu", 24))
my_button.grid(column=1, row=3, sticky=SW)

root.mainloop()
