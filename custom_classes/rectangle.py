
#Topic: Custom Classes in Python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    # Define the iterator method
    def __iter__(self):
        # Here yield two dictionaries, first with length, then with width
        yield {'length': self.length}
        yield {'width': self.width}

# Example use:
rectangle = Rectangle(5, 10)

# Iterating over the rectangle
for dimension in rectangle:
    print(dimension)
