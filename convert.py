import requests
import json

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
    def convert_to(cls):
        currency_code = input("""
Which currency_code would you like to convert to? 
(format: 3-letters capitalized, ex:AUD)
Input 1 for available currencies\n\n""")
        if currency_code in cls.current_rates:
            return cls.current_rates[currency_code]
        elif currency_code == "1":
            cls.currencies_available()
        cls.convert_to()
    
    @classmethod    
    def convert_from(cls):
        currency_code = input("""
Which currency_code would you like to convert from? 
(format: 3-letters capitalized, ex:AUD)\n
Input 1 for available currencies\n\n""")
        if currency_code in cls.current_rates:
            return cls.current_rates[currency_code]
        elif currency_code == "1":
            cls.currencies_available()
        cls.convert_from()
        
    def convert(self, currency_code_to, currency_code_from):
        return 1000*currency_code_to/currency_code_from
        
        
        
        
        
        
        
        
        
        
        
        
        
    