import unittest
from convert import CurrencyConverter

class TestCurrencyConverterClass(unittest.TestCase):
    def test_get_current_rates(self):
        """Test get_current_rates()"""
        CurrencyConverter.get_current_rates()
        self.assertEqual(type(CurrencyConverter.current_rates), dict)
        
        
    #def test_currencies_available(self):
    #"""Test currencies_available()"""
    #test the print function
    
        
    # def test_get_currency_code(self):
    #     """Test get_currency_code"""
    #     CurrencyConverter.get_current_rates()
    #     self.assertEqual(type(CurrencyConverter.get_currency_code()), str)

    def test_get_currency_rate(self):
        """Test get_currency_rates()"""
        CurrencyConverter.get_current_rates()
        self.assertEqual(type(CurrencyConverter.get_currency_rate("CAD")), float)
        
        
        