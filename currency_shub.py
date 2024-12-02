from tkinter import *
from tkinter import ttk
import requests
import json
from PIL import Image, ImageTk

# Colors (changed to blue shades)
cor0 = "#E0F7FA"  # Light blue background for the main window
cor1 = "#01579B"  # Dark blue text color
cor2 = "#0288D1"  # Blue button and header background color

window = Tk()
window.geometry('315x400')
window.title('Converter')
window.configure(bg=cor2)
window.resizable(height=FALSE, width=FALSE)

# Title label
label = Label(window, text='Currency Converter', height=3, bg=cor2, fg='white', font=('Ivy 12 bold')).place(x=85, y=0)

# Top frame
top = Frame(window, width=500, height=60, bg=cor2)
top.grid(row=0, column=1)

# Main frame
main = Frame(window, width=500, height=400, bg=cor0)
main.grid(row=1, column=0)

# Convert function
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    # Input currencies and amount
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    # Querystring with correct variable usage
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    # Headers for RapidAPI
    headers = {
        "x-rapidapi-key": "c9a9b32df0msh3454297ef156af1p127862jsn3085881a44ac",  # Replace with your valid API key
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=querystring)

    # Ensure the request was successful
    if response.status_code == 200:
        try:
            # Parse the response JSON
            data = response.json()

            # Extract the converted amount
            if "result" in data and "convertedAmount" in data["result"]:
                converted_amount = data["result"]["convertedAmount"]
                formatted = "{:,.2f}".format(converted_amount)
                result['text'] = f"{formatted} {currency_2}"
            else:
                result['text'] = "Error: Data not found"
        except json.JSONDecodeError:
            result['text'] = "Failed to decode JSON"
    else:
        result['text'] = "Request failed"
        print(f"Request failed with status code {response.status_code}: {response.text}")

# Top frame label (app name)
app_name = Label(top, text='Currency Converter', height=5, padx=13, pady=30, anchor=CENTER, bg=cor2, fg='white')
app_name.place(x=1, y=0)

# Main frame result label
result = Label(main, text="", width=17, height=2, pady=7, relief=SOLID, anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

# Currency list
currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']

# "From" label and combo box
from_label = Label(main, text="From", width=8, height=1, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1['values'] = currency
combo1.place(x=50, y=115)

# "To" label and combo box
to_label = Label(main, text="To", width=8, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = currency
combo2.place(x=168, y=115)

# Amount entry
value = Entry(main, width=23, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
value.place(x=50, y=190)

# Convert button
button = Button(main, text="Convert", width=20, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), command=convert)
button.place(x=50, y=240)

window.mainloop()
