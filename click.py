from tkinter import *

root = Tk()
root.title("Click Counter")
count = 0


def increase():
    global count
    count += 1
    counter.configure(text=f"Your count is: {count}")


counter = Label(text=f"Your count is: {count}")
counter.grid()
button = Button(text="Click to increase", command=increase)
button.grid()

root.mainloop()
