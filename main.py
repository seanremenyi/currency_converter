import requests
import json
from convert import Currency_converter

new_request = Currency_converter()
new_request.get_current_rates()

print("""\nWhich currency would you like to convert to?\nFormat: 3 Capitalized letters, Ex: AUD\n(Type 1 for list of avaiable currencies)\n""")
currency_code_to = new_request.get_currency_code()


print("""\nWhich currency are you converting from?\nFormat: 3 Capitalized letters, Ex: AUD\n(Type 1 for list of avaiable currencies)\n""")
currency_code_from = new_request.get_currency_code()


amount = input("\nHow much money would you like to convert?\n")
while True:
    try:
        amount = float(amount)
        break
    except:
        amount = input("Needs to be a number\nHow much do you want to convert")


currency_rate_to = new_request.get_currency_rate(currency_code_to)
currency_rate_from = new_request.get_currency_rate(currency_code_from)
converted_value = new_request.convert(amount, currency_rate_to, currency_rate_from)

print(f"\n{amount} {currency_code_from} is {converted_value} in {currency_code_to}\n")







