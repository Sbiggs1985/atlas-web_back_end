#!/usr/bin/env python3

import logging

""" 5 Standard Logging Levels below!
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

"""Basic Configuration Change"""
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add Function"""
    return x + y
    
def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y
    
def divide(x, y):
    """Divide Function"""
    return x / y
    
num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Add: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Add: {} * {} = {}'.format(num_1, num_2, sub_result))

div_result = divide(num_1, num_2)
logging.debug('Add: {} / {} = {}'.format(num_1, num_2, sub_result))


"""Special Format Codes link"""
"""Can change format in our log"""
"""https://docs.python.org/3/library/logging.html#logrecord-attributes"""

"""Next video!!!666666666666666666666666666666666666666666666"""
"""Issues can arise because it always shares the logger"""
"""Creating separate loggers, adding handlers, and formatters."""
"""https://youtu.be/jxmzY9soFXg?si=HudVr4xRBWFx28SJ"""