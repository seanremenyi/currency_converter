import requests
import json

class Currency_converter():
    current_rates = []
    
    @classmethod
    def get_current_rates(cls):
        response = requests.get("https://api.exchangeratesapi.io/latest")
        json_text = json.loads(response.text)
        cls.current_rates = json_text["rates"]
        
    
    # def __init__(self,data):
    #     self.data = data
    @staticmethod
    def currencies_available():
        return f"CAD\nHKD\nISK\nPHP\nDKK\nHUF\nCZK\nAUD\nRON\nSEK\nIDR\nINR\nBRL\nRUB\nHRK\nJPY\nTHB\nCHF\nSGD\nPLN\nBGN\nTRY\nCNY\nNOK\nNZD\nZAR\nUSD\nMXN\nILS\nGBP\nKRW\nMYR"
    # def convert_to(self, currency_code):
    #     return self.data["rates"][currency_code]
        
    # def convert_from(self, currency_code):
    #     return self.data["rates"][currency_code]

    # def convert(self, currency_code_to, currency_code_from)
    