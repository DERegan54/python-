"""Python serial number generator."""

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

    def __init__(self, start=0):
        """Make new instance of SerialGenerator beginning at start."""

        self.start = self.next = start

    def __repr__(self):
        """Display representation."""
        return f"<SerialGenerator start={self.start} next={self.next}>" 

    def generate(self):
        """ Generates a new serial number beginning at start and incrementing by 1. """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ Resets start.next to the start value. """
        self.next = self.start
        
   