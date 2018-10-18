import tkinter as tk
from tkinter import messagebox


def hello():
    messagebox.showinfo('Say Hello', 'Hello World')


if __name__ == '__main__':

    top = tk.Tk()
    top.title('Demo 1b')
    top.geometry('200x100')
    B1 = tk.Button(top, text='Say Hello', width=10, command=hello)
    B1.place(x=50, y=30)
    top.mainloop()


