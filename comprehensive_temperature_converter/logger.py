import logging

# Set up logging configuration
logging.basicConfig(
    filename='temperature_conversion.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_conversion(input_temp, input_unit, result, result_unit):
    """
    Log the temperature conversion details.
    """
    logging.info(f"Converted {input_temp} {input_unit} to {result} {result_unit}")
