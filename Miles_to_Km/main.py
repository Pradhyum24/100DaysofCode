from tkinter import *

window = Tk()
window.minsize(width=300,height=150)
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    label_output.config(text=km,justify="center")
    print(km)


input = Entry(width=10)
input.grid(row=0,column=1)

label1 = Label(text="Miles")
label1.grid(row=0,column=2)
label1.config()

label2 = Label(text="is equal to")
label2.grid(row=1,column=0)

label_output = Label(text="")
label_output.grid(row=1,column=1)

label3 = Label(text="Km")
label3.grid(row=1,column=2)

button = Button(text="Calculate",command=miles_to_km)
button.grid(row=2,column=1)

window.mainloop()
