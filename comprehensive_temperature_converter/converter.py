from logger import log_conversion

def celisus_to_fahrenheit(celsius):
    """
    this is a function that converts
    temprature from celsius scale to farhanite scale
    """
    fahrenheit = (celsius *9/5) + 32
    log_conversion(celsius, "Celsius", fahrenheit, "Fahrenheit")
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
   """
   this is a function that converts
   temprature from farhanite scale to celsius scale
   """
   celsius= (fahrenheit -32) *5/9
   log_conversion(fahrenheit, "Fahrenheit", celsius, "Celsius")
   return celsius

def celcius_to_kalvin(celsius):
    """
    this is a function that converts
    temprature from celsius scale to kalvin scale
    """
    kalvin = celsius + 273.15
    log_conversion(celsius, "Celsius", kalvin, "Kelvin")
    return kalvin

def kalvin_to_celcius(kalvin):
    """
    this is a function that converts
    temprature from kalvin scale to celsius scale 
    """
    celsius = kalvin - 273.15
    log_conversion(kalvin, "Kelvin", celsius, "Celsius")
    return celsius
    
def fahrenheit_to_kalvin(fahrenheit):
    """
    this is a function that converts
    temprature from fahrenheit scale to kalvin scale
    """
    kalvin = 5/9 * (fahrenheit - 32) + 273.15
    log_conversion(fahrenheit, "Fahrenheit", kalvin, "Kelvin")
    return kalvin

def kalvin_to_fahrenheit(kalvin):
    """
    this is a function that converts
    temprature from kalvin scale to fahrenheit scale
    """
    fahrenheit = 9/5 * (kalvin - 273.15) + 32
    log_conversion(kalvin, "Kelvin", fahrenheit, "Fahrenheit")
    return fahrenheit