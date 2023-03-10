from tkinter import *

window = Tk()
window.minsize(width=350,height=100)
window.title("Miles to Kilometer Converter")
window.config(padx=100, pady=50)

def calculate():
  answer = round(int(input.get()) * 1.609)
  answer_label.config(text=str(answer))
  

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to ")
equal_label.config(pady=10)
equal_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.config(padx=10)
answer_label.grid(column=1, row=1)

kil_label = Label(text="KM")
kil_label.config(padx=10)
kil_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=calculate)
cal_button.grid(column=1, row=2)

window.mainloop()