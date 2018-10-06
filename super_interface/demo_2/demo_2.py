import tkinter as tk
from tkinter import messagebox


def bye():
    messagebox.showinfo('Say Bye', 'Good Bye!')


if __name__ == '__main__':
    top = tk.Tk()
    top.title('Demo 2')
    top.geometry('200x100')
    B1 = tk.Button(top, text='Say Bye', width=10, command=bye)
    B1.place(x=50, y=30)
    top.mainloop()
