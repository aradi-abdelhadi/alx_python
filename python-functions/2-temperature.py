#!/usr/bin/env python3

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    :param fahrenheit: Temperature in Fahrenheit.
    :return: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

