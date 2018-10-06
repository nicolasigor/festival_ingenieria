import tkinter as tk
from tkinter import messagebox


def whatsup():
    messagebox.showinfo("Say What's up", "What's up!")


if __name__ == '__main__':
    top = tk.Tk()
    top.title('Demo 3')
    top.geometry('200x100')
    B1 = tk.Button(top, text="Say What's up", width=10, command=whatsup)
    B1.place(x=50, y=30)
    top.mainloop()
