import argparse
from converter import celisus_to_fahrenheit, fahrenheit_to_celsius, celcius_to_kalvin, kalvin_to_celcius, fahrenheit_to_kalvin, kalvin_to_fahrenheit
from logger import log_conversion

def convert_temperature(input_temp, input_unit, output_unit):
    """
    Convert the temperature based on input and output units.
    """
    if input_unit == "Celsius":
        if output_unit == "Fahrenheit":
            result = celisus_to_fahrenheit(input_temp)
        elif output_unit == "Kelvin":
            result = celcius_to_kalvin(input_temp)
        else:
            result = input_temp  # Celsius to Celsius
    elif input_unit == "Fahrenheit":
        if output_unit == "Celsius":
            result = fahrenheit_to_celsius(input_temp)
        elif output_unit == "Kelvin":
            result = fahrenheit_to_kalvin(input_temp)
        else:
            result = input_temp  # Fahrenheit to Fahrenheit
    elif input_unit == "Kelvin":
        if output_unit == "Celsius":
            result = kalvin_to_celcius(input_temp)
        elif output_unit == "Fahrenheit":
            result = kalvin_to_fahrenheit(input_temp)
        else:
            result = input_temp  # Kelvin to Kelvin
    else:
        raise ValueError("Invalid input unit. Must be 'Celsius', 'Fahrenheit', or 'Kelvin'.")

    # Log the conversion
    log_conversion(input_temp, input_unit, result, output_unit)
    
    return result

def main():
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Temperature Converter")
    parser.add_argument("input_temp", type=float, help="The temperature value to convert.")
    parser.add_argument("input_unit", choices=["Celsius", "Fahrenheit", "Kelvin"], help="The unit of the input temperature.")
    parser.add_argument("output_unit", choices=["Celsius", "Fahrenheit", "Kelvin"], help="The unit of the output temperature.")
    
    args = parser.parse_args()

    # Perform conversion
    converted_temp = convert_temperature(args.input_temp, args.input_unit, args.output_unit)

    # Print the result
    print(f"{args.input_temp} {args.input_unit} is equal to {converted_temp} {args.output_unit}")

if __name__ == "__main__":
    main()
