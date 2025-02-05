import unittest
from comprehensive_temperature_converter.converter import celisus_to_fahrenheit
class TestConverter(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(celisus_to_fahrenheit(0), 32)
        self.assertEqual(celisus_to_fahrenheit(100), 212)
        self.assertEqual(celisus_to_fahrenheit(25.5), 77.9, places=2)

if __name__ == '__main__':
    unittest.main()
    
       
