import tkinter as tk

win = tk.Tk()
win.title("My Buttons")
win.geometry("300x200")

def say_hello():
    print("Hello World!")

btn = tk.Button(win, text="exet", command=say_hello)
btn.pack(pady=20)

win.mainloop()