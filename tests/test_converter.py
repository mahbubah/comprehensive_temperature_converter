import unittest
from comprehensive_temperature_converter.converter import (celisus_to_fahrenheit, fahrenheit_to_celsius, 
                       celcius_to_kalvin, kalvin_to_celcius, 
                       fahrenheit_to_kalvin, kalvin_to_fahrenheit)
class TestConverter(unittest.TestCase):
     # Test Celsius to Fahrenheit
    def test_celsius_to_fahrenheit(self):
        # Normal cases
        self.assertEqual(celisus_to_fahrenheit(0), 32)
        self.assertEqual(celisus_to_fahrenheit(100), 212)
        
        # Edge case (absolute zero)
        self.assertEqual(celisus_to_fahrenheit(-273.15), -459.67)
    
    # Test Fahrenheit to Celsius
    def test_fahrenheit_to_celsius(self):
        # Normal cases
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        
        # Edge case (absolute zero)
        self.assertEqual(fahrenheit_to_celsius(-459.67), -273.15)

    # Test Celsius to Kelvin
    def test_celsius_to_kelvin(self):
        # Normal cases
        self.assertEqual(celcius_to_kalvin(0), 273.15)
        self.assertEqual(celcius_to_kalvin(100), 373.15)
        
        # Edge case (absolute zero)
        self.assertEqual(celcius_to_kalvin(-273.15), 0)
        
    # Test Kelvin to Celsius
    def test_kelvin_to_celsius(self):
        # Normal cases
        self.assertEqual(kalvin_to_celcius(273.15), 0)
        self.assertEqual(kalvin_to_celcius(373.15), 100)
        
        # Edge case (absolute zero)
        self.assertEqual(kalvin_to_celcius(0), -273.15)
    
    # Test Fahrenheit to Kelvin
    def test_fahrenheit_to_kelvin(self):
        # Normal cases
        self.assertEqual(fahrenheit_to_kalvin(32), 273.15)
        self.assertEqual(fahrenheit_to_kalvin(212), 373.15)
        
        # Edge case (absolute zero)
        self.assertEqual(fahrenheit_to_kalvin(-459.67), 0)

    # Test Kelvin to Fahrenheit
    def test_kelvin_to_fahrenheit(self):
        # Normal cases
        self.assertEqual(kalvin_to_fahrenheit(273.15), 32)
        self.assertEqual(kalvin_to_fahrenheit(373.15), 212)
        
        # Edge case (absolute zero)
        self.assertEqual(kalvin_to_fahrenheit(0), -459.67)
    
    # Test for invalid input types (non-numeric input)
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            celisus_to_fahrenheit("string")
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("string")
        with self.assertRaises(TypeError):
            celcius_to_kalvin("string")
        with self.assertRaises(TypeError):
            kalvin_to_celcius("string")
        with self.assertRaises(TypeError):
            fahrenheit_to_kalvin("string")
        with self.assertRaises(TypeError):
            kalvin_to_fahrenheit("string")
    
if __name__ == "__main__":
    unittest.main()
    
       
