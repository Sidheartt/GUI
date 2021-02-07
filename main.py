from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


#Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack(side="top")
#my_label.place(x=150,y=0)
my_label.grid(column=0, row=0)

button = Button(text="New Button", command=button_clicked)
#button.pack()
button.grid(column=2,row=0)

#button
button = Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1,row=1)

#Entry
input = Entry(width=10)
input.get()
#input.pack()
input.grid(column=1 , row=2)



window.mainloop()
