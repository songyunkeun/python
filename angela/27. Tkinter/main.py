from tkinter import *

window = Tk()
window.wm_title("MY First GUI Program")
window.wm_minsize(500, 300)
window.config(padx=100, pady=100)

my_entry = Entry(width=10)
my_entry.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=0)

my_label2 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Arial", 24, "bold"))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="km", font=("Arial", 24, "bold"))
my_label4.grid(column=2, row=1)


def button_clicked():
    km = float(my_entry.get()) * 1.609
    my_label3.config(text=km)
    #my_label['text'] = my_entry.get()

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()