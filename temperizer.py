"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c

def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temp_f = (9/5 * temperature_c) + 32
    return temp_f

def convert_c_to_k(temperature_c):
    """Convert Celcius to Kelvin"""
    temp_k = temperature_c + 273.15
    return temp_k

def convert_f_to_k(temperature_f):
    """Convert Fahrenheit to Kelvin"""
    temp_k = (temperature_f + 459.67) / 1.8
    return temp_k
    
def convert_k_to_c(temperature_k):
    """Convert Kelvin to Celcius"""
    temp_c = temperature_k - 273.15 
    return temp_c
    
def convert_k_to_f(temperature_k):
    """Convert Kelvin to Fahrenheit"""
    temp_f = temperature_k * 1.8 - 459.67
    return temp_f