from tkinter import *  # importing tkinter module
from tkinter import ttk  # importing ttk module
from tkinter import messagebox  # importing messagebox for notifications
from PIL import Image, ImageTk  # importing Pillow for Image processing


# SuperClass for Background Image and Self-Centering window
class Main:
    def __init__(self, root):
        self.root = root
        # Setting Background Image in a Canvas
        self.BG = Canvas(self.root, highlightthickness=0)
        self.BG.pack(fill=BOTH, expand=1)
        # Event Checker to resize the Image whenever window size is changed
        self.BG.bind("<Configure>", self.resize_image)
        self.img = ImageTk.PhotoImage(Image.open('D:\\Users\\HIRANMAY-PC\\Downloads\\img.jpeg'))
        self.canvas_img = self.BG.create_image(0, 0, anchor="nw", image=self.img)

    def resize_image(self, event):
        photo = Image.open('D:\\Users\\HIRANMAY-PC\\Downloads\\img.jpeg')
        # Resizing Image using inbuilt Canvas Resize method
        img = photo.resize((event.width, event.height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.BG.itemconfig(self.canvas_img, image=self.img)

    def center(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        # Calculating the Centre of the Screen
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 75
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class Login(Main):
    def __init__(self, root):
        Main.__init__(self, root)
        self.root.maxsize(400, 400)
        self.root.title("Hello World")
        self.f_name = self.BG.create_text((100, 100), text="HELLO NIGGAS", fill="white")
        self.center()


if __name__ == '__main__':
    Login_Window = Tk()
    Login_Window_Widget = Login(Login_Window)
    Login_Window.mainloop()
