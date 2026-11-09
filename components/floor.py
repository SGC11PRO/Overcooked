class Floor:
    """ Docs... """
    def __init__(self, x_position: int, y_position: int):
        """
        Init method
        :param x_position: x position
        :param y_position: y position
        """

        self.x = x_position
        self.y = y_position

        # image (bank, x, y, width, height)
        self.image = (0, 0, 240, 16, 16)


    # ERROR HANDLING -------------------------------------
    # properties
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y


    # setters
    @x.setter
    def x (self, x:int):
        if not isinstance(x, int):
            raise TypeError('x position must be an int')
        elif x < 0:
            raise ValueError('x position must be positive')
        else:
            self.__x = x

    @y.setter
    def y (self, y:int):
        if not isinstance(y, int):
            raise TypeError('y position must be an int')
        elif y < 0:
            raise ValueError('y position must be positive')
        else:
            self.__y = y
        