from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=400)
window.config(padx=40, pady=40)

def miles_to_km():
    miles = float(input_miles.get())
    
    # if miles not NUMERIC:
    #     miles = 0
    # miles += miles
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")
    # print("Calculating miles to km")

input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

equate_label = Label(text="is equal to", font=("Arial", 16))
equate_label.grid(column=0, row=1)


km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="0")
# #Gets text in entry
# print(entry.get())
# entry.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()