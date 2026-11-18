from components.stations.station import Station

class Floor:
    """This class will store the floor layout of the game, and will draw it on the screen. 
    It will also store the stations that are on the floor, and will draw them on the screen."""

    def __init__(self):

        self.x = 0
        self.y = 32

        # "oni": Onion, "egg": Egg, "cho": Chorizo, "tom": Tomato, "pot": Potato
        # "brd": Board, "ble": Blender, "pan": Pan, "plt": Plates, "srv": Serve
        # "pss": Pass, "bin": Bin, "snk": Sink, "rtn": Return
        # "fre": Free, "wal": Wall

        # (read-only)
        self.__LAYOUT = (
            ("oni", "egg", "cho", "fre", "brd", "fre", "ble", "fre", "fre", "fre", "fre", "srv"),
            (12 * ("",)), (12 * ("",)), (12 * ("",)),
            ("wal", "pss", "wal", "pss", "wal", "bin", "wal", "pss", "wal", "snk", "pss", "wal"),
            (12 * ("",)), (12 * ("",)), (12 * ("",)),
            ("tom", "pot", "fre", "fre", "fre", "brd", "fre", "pan", "rtn", "plt", "fre", "fre")
        )

    def draw(self, row):
        """This method will draw the floor on the screen (executed every frame)"""
        for station in range(len(self.__LAYOUT[row])):
            Station(16 * station, 16 * row + 32, self.__LAYOUT[row][station]).draw()



    # ERROR HANDLING ----------------------------------------
    # properties
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property 
    def layout(self) -> tuple:
        return self.__LAYOUT


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
        