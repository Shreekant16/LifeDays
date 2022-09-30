from tkinter import *

window = Tk()


def cal():
    age = int(entry.get())
    years_remaining = 100 - age
    label1 = Label(text=f"Days remaining are : {years_remaining * 365} (approx)\n"
                        f"Moths remaining are : {years_remaining * 12}\n"
                        f"Weeks remaining are : {years_remaining * 52}\n")
    label1.grid(column=1, row=2)


window.geometry('400x200')
label = Label(text="age : ")
label.grid(column=0, row=0)
entry = Entry(width=50)
entry.grid(column=1, row=0)
button = Button(text="SUBMIT", width=10, command=cal)
button.grid(column=1, row=1)

window.mainloop()
