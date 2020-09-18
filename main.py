import requests
import json
from convert import Currency_converter

new_request = Currency_converter()
new_request.get_current_rates()


print("""
Which currency would you like to convert to?
Format: 3 Capitalized letters, Ex: AUD
(Type 1 for list of avaiable currencies)
""")
convert_to_code = new_request.get_currency_code()


print("""
Which currency are you converting from?
Format: 3 Capitalized letters, Ex: AUD
(Type 1 for list of avaiable currencies)
""")
convert_from_code = new_request.get_currency_code()


# convert_from = new_request.convert_from()
# convert_to = new_request.convert_to()


# final = new_request.convert(convert_to, convert_from)
# print(convert_to)
# print(convert_from)
# print(final)

# print(new_request.current_rates("success"))

# currency_to = new_request.convert_to("CAD")
# currency_from = new_request.convert_from("AUD")
# print(f" CAD : {currency_to}, AUD: {currency_from}")


# users_current_currency = input("What currency do you have?")
# users_wanted_currency = input("What currency do you want?")


