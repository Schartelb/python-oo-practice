"""Python serial number generator."""

from ast import increment_lineno
from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.increment = start

    def __repr__(self):
        return f"The number entered was {self.start}, the current number is {self.increment}"

    def generate(self):
        'increments number up by 1'
        self.increment += 1
        return self.increment

    def reset(self):
        'returns increment to starting number'
        self.increment = self.start
        return self.increment
