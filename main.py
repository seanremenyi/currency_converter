import requests
import json
from convert import Currency_converter

new_request = Currency_converter()
new_request.get_current_rates()


print("""\nWhich currency would you like to convert to?\nFormat: 3 Capitalized letters, Ex: AUD\n(Type 1 for list of avaiable currencies)\n""")
currency_code_to = new_request.get_currency_code()


print("""\nWhich currency are you converting from?Format: 3 Capitalized letters, Ex: AUD\n(Type 1 for list of avaiable currencies)\n""")
currency_code_from = new_request.get_currency_code()


amount = input("How much money would you like to convert?")
while type(amount) != float or type(amount)!=int:
    amount = input("Needs to be a number\nHow much do you want to convert")


currency_value_to = new_request.get_currency_value(currency_code_to)
currency_value_from = new_request.get_currency_value(currency_code_from)
new_request.convert(amount, currency_code_to, currency_value_from)
