import requests
import json
from decorators import format

class Currency_converter():
    current_rates = []
    
    @classmethod
    def get_current_rates(cls):
        response = requests.get("https://api.exchangeratesapi.io/latest")
        json_text = json.loads(response.text)
        cls.current_rates = json_text["rates"]
        
    @staticmethod
    def currencies_available():
        print(f"CAD\nHKD\nISK\nPHP\nDKK\nHUF\nCZK\nAUD\nRON\nSEK\nIDR\nINR\nBRL\nRUB\nHRK\nJPY\nTHB\nCHF\nSGD\nPLN\nBGN\nTRY\nCNY\nNOK\nNZD\nZAR\nUSD\nMXN\nILS\nGBP\nKRW\nMYR")
    
    @classmethod
    def get_currency_code(cls):
        currency_code = input()
        while currency_code not in cls.current_rates:
            if currency_code == "1":
                cls.currencies_available()
            currency_code = input("try again\n")
        return currency_code
        
    @classmethod
    def get_currency_rate(cls, currency_code):
        return cls.current_rates[currency_code]
    
    @format    
    def convert(self, amount, currency_rate_to, currency_rate_from):
        return amount*currency_rate_to/currency_rate_from
        

        
        
        
        
        
        
        
        
        
        
        
        
    