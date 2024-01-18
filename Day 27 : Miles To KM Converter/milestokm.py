from tkinter import *

window = Tk()
window.title("Miles To Kilometers Converter")
window.config(padx=20, pady=20)

def converter():
    miles = float(input.get())
    km = miles * 1.60934
    value_label["text"] = str(km)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="Is Equal To")
equal_label.grid(column=0, row=1)

value_label = Label(text="")
value_label.grid(column=1, row=1)

km_label = Label(text="Kms")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
