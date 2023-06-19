import requests
import json

# API URL for retrieving exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/"

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    # Make API request to get exchange rates
    response = requests.get(API_URL + from_currency)
    data = json.loads(response.text)
    
    # Check if API request was successful
    if response.status_code == 200:
        # Get exchange rate for the target currency
        exchange_rate = data["rates"][to_currency]
        
        # Calculate the converted amount
        converted_amount = amount * exchange_rate
        
        return converted_amount
    else:
        return None

# Function to display available currencies
def display_currencies():
    response = requests.get(API_URL)
    data = json.loads(response.text)
    
    if response.status_code == 200:
        currencies = data["rates"]
        print("Available Currencies:")
        for currency in currencies:
            print(currency)
    else:
        print("Failed to retrieve currency data.")

# Main program
print("Currency Converter")

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount:
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
else:
    print("Failed to perform currency conversion.")

# Additional features can be implemented here

