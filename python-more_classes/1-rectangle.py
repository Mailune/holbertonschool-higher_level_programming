class Rectangle:
    """Class defining a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method to retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
