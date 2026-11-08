import pyxel

class Timer:
    """ A timer. Can be used for the global timer or for individual
    timers for each order"""
    def __init__(self, total_seconds: int):
        """
        :param x: x position of the text
        :param y: y position of the text
        :param s: seconds
        """
        self.total_seconds = total_seconds
        

    def decrese(self, s: int):
        """ Decrese s seconds
        :param s: seconds to decrease
        """
        if self.total_seconds >= s:
            self.total_seconds -= s
        else:
            self.total_seconds = 0

    def draw_timer(self, x: int, y: int, col: int):
        """
        :param x: x position
        :param y: y position
        :param col: text color
        """
        if not isinstance(x, int):
            raise TypeError("x position must be an integer")
        elif x < 0:
            raise ValueError("x position must be positive")

        if not isinstance(y, int):
            raise TypeError("y position must be an integer")
        elif y < 0:
            raise ValueError("y position must be positive")

        self.m = self.total_seconds // 60
        self.s = self.total_seconds % 60
        
        pyxel.text(x, y, f"{self.m}:{self.s:02}", col)



    # ERROR HANDLING ------------------------------------
    # properties
    @property
    def total_seconds(self) -> int:
        return self.__total_seconds

    # setters
    @total_seconds.setter
    def total_seconds(self, total_seconds: int):
        if not isinstance(total_seconds, int):
            raise TypeError("Seconds must be an integer")
        elif total_seconds < 0:
            raise ValueError("Seconds must be positive")
        else:
            self.__total_seconds = total_seconds