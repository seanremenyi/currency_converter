import requests
import json

class Currency_converter():
    
    def __init__(self,data):
        self.data = data
        
    def convert_to(self, currency_code):
        return self.data["rates"][currency_code]





def get_response():
    response = requests.get("http://data.fixer.io/api/latest?access_key=7afe03ee50cf06a98045037e8bed6a24")
    json_text = json.loads(response.text)
    if json_text["success"] == True:
        return json_text
    get_response()
    
new_request = Currency_converter(get_response())

print(new_request.convert_to("CAD"))