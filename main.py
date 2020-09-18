import requests
import json
from convert import Currency_converter


# def get_response():
#     response = requests.get("http://data.fixer.io/api/latest?access_key=7afe03ee50cf06a98045037e8bed6a24")
#     json_text = json.loads(response.text)
#     if json_text["success"] == True:
#         return json_text
#     get_response()
    

    
new_request = Currency_converter()
new_request.get_current_rates()
print(new_request.current_rates)
print(new_request.currencies_available())
# print(new_request.current_rates("success"))

# currency_to = new_request.convert_to("CAD")
# currency_from = new_request.convert_from("AUD")
# print(f" CAD : {currency_to}, AUD: {currency_from}")


# users_current_currency = input("What currency do you have?")
# users_wanted_currency = input("What currency do you want?")


