from tkinter import *  # importing tkinter module
from tkinter import ttk  # importing ttk module
from tkinter import messagebox  # importing messagebox for notifications
from PIL import Image, ImageTk  # importing Pillow for Image processing


# SuperClass for Background Image and Self-Centering window
class Main:
    def __init__(self, root):
        self.root = root
        # Importing BG Image
        image = Image.open('D:\\Users\\HIRANMAY-PC\\Downloads\\img.jpeg')
        self.copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        self.label = ttk.Label(self.root, image=photo)
        # Background image resizing
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=BOTH, expand=YES)
        # Centering the Window
        self.center()

    def resize_image(self, event):
        # Getting height and width of resized window
        new_width = event.width
        new_height = event.height
        # Resizing Image
        image = self.copy_of_image.resize((new_width - 5, new_height - 5))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # avoid garbage collection

    def center(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        # Calculating the Centre of the Screen
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 75
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == '__main__':
    Login_Window = Tk()
    Login_Window.title("Title")
    Login_Window.configure(bg="black")
    Login_Window.geometry('300x300')
    Login_Window_Widget = Main(Login_Window)
    Login_Window.mainloop()
