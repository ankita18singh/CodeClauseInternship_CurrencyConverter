from tkinter import* 
import tkinter as tk

conversion_inr = {
    "INR": {}
}
with open('currency_data.txt') as f:
    lines = f.readlines()

conversion_table = {}
for line in lines:
    parsed = line.split("\t")
    conversion_table[parsed[0]] = parsed[1]
def convert_currency():
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    if base_currency == target_currency:
        converted_amount = amount
    else:
        converted_amount = amount *float(conversion_table[target_currency])

    result_label.config(text=str(converted_amount))

window = tk.Tk()
window.title("Currency Converter")
window.geometry("600x600")

label1 = tk.Label(window, text="Amount :")
label1.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="Base Currency :")
label2.pack()

base_currency_var = tk.StringVar()
base_currency_var.set("INR")

base_currency_menu=tk.OptionMenu(window,base_currency_var,*conversion_inr.keys())
base_currency_menu.pack()

label3 = tk.Label(window, text="Target Currency :")
label3.pack()

target_currency_var = tk.StringVar()
target_currency_var.set("EURO")

target_currency_menu=tk.OptionMenu(window,target_currency_var,*conversion_table.keys())
target_currency_menu.pack()

label4 = tk.Label(window, text="Converted Amount:")
label4.pack()

result_label = tk.Label(window, text="")
result_label.pack()

button = tk.Button(window, text="Convert", command=convert_currency)
button.pack()

window.mainloop()
