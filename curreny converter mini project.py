#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox

# Create a function to convert currency
def convert():
    # Get the amount and currencies from the user
    amount = amount_entry.get()

    if not amount.isnumeric() and not amount.replace(".", "", 1).isdigit():
        messagebox.showerror("Invalid Amount", "Please enter a valid numeric amount.")
        return

    amount = float(amount)
    from_currency = from_currency_menu.get()
    to_currency = to_currency_menu.get()

    # Create a dictionary of currency conversion rates
    rates = {'USD': 1.0, 'EUR': 0.82, 'GBP': 0.71, 'JPY': 108.84, 'INR': 74.97}

    # Convert the amount to the desired currency
    converted_amount = amount / rates[from_currency] * rates[to_currency]

    # Display the converted amount in the result label
    result_label.config(text=f"{converted_amount:.2f} {to_currency}")

# Create a function to clear the amount_entry and result_label widgets
def clear():
    amount_entry.delete(0, END)
    result_label.config(text="")

# Create a GUI window
window = Tk()
window.title("Currency Converter using Tkinter")
window.geometry('390x320')
window.configure(bg='#9ac9ff')

# Create labels and entry widgets for the amount, from currency, and to currency
amount_l1 = Label(window, text="Currency Converter", font=('Arial', 14, 'bold'), bg='#9ac9ff')
amount_l1.grid(row=0, column=0,columnspan=5, padx=100, pady=10)

amount_label = Label(window, text="Amount:", font=('Arial', 14, 'bold'), bg='#9ac9ff')
amount_label.grid(row=1, column=0, padx=10, pady=10)
amount_entry = Entry(window, font=('Arial', 14), width=10)
amount_entry.grid(row=1, column=1, padx=10, pady=10)

from_currency_label = Label(window, text="From Currency:", font=('Arial', 14, 'bold'), bg='#9ac9ff')
from_currency_label.grid(row=2, column=0, padx=10, pady=10)
from_currency_menu = StringVar(window)

from_currency_dropdown = OptionMenu(window, from_currency_menu, 'USD', 'EUR', 'GBP', 'JPY', 'INR')
from_currency_dropdown.config(font=('Arial', 14), bg='#7fffd4')
from_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

to_currency_label = Label(window, text="To Currency:", font=('Arial', 14, 'bold'), bg='#9ac9ff')
to_currency_label.grid(row=3, column=0, padx=10, pady=10)
to_currency_menu = StringVar(window)

to_currency_dropdown = OptionMenu(window, to_currency_menu, 'USD', 'EUR', 'GBP', 'JPY', 'INR')
to_currency_dropdown.config(font=('Arial', 14), bg='#7fffd4')
to_currency_dropdown.grid(row=3, column=1, padx=10, pady=10)

# Create a button to convert currency
convert_button = Button(window, text="Convert", font=('Arial', 14, 'bold'), bg='#ffcdb2', command=convert)
convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


clear_button = Button(window, text="Clear", font=('Arial', 14, 'bold'), bg='#ffcdb2', command=clear)
clear_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
                  
result_label = Label(window, font=('Arial', 14), bg='#9ac9ff')
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
                  
window.mainloop()


# In[ ]:




