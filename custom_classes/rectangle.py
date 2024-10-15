
#Topic: Custom Classes in Python
class Rectangle:
    """ A class to represent a rectangle with length and width attributes.
    This class also implements an iterator to iterate over the rectangle's dimensions,
    yielding the length and width as dictionaries."""

    def __init__(self, length: int, width: int):
        """
        Constructor for the Rectangle class.
        Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.
        Initializes the length and width attributes of the rectangle."""

        self.length = length
        self.width = width
    
    # Define the iterator method
    def __iter__(self):

        """This method makes the Rectangle class iterable by defining a custom iterator.
        The method uses the 'yield' keyword to return dictionaries containing 
        the length and width of the rectangle one at a time.
        This allows iteration over the rectangle's dimensions."""


        # First yield the length as a dictionary
        yield {'length': self.length}
        # Then yield the width as a dictionary
        yield {'width': self.width}

# Example use:
rectangle = Rectangle(5, 10) # Create a rectangle object with length 5 and width 10

# Iterating over the rectangle
for dimension in rectangle:
    """ This loop demonstrates iterating over the Rectangle object.
    Since the __iter__ method yields the length and width as separate dictionaries,
    each iteration will print a dictionary with either the length or the width."""
    print(dimension)
