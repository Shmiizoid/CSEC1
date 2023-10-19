import tkinter as tk

def print_hello_world():
    print("hello world")

def exit_application():
    root.destroy()

root = tk.Tk()

hello_button = tk.Button(root, text="Print Hello World", command=print_hello_world)
hello_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack()

root.mainloop()