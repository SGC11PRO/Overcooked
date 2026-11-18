import pyxel

class Station:
    """ This class will store a station instance, without a texture.
    It will adjust according to what type of station it is.
    Examples are cutting boards, blenders, pan, ingredient drawer, free worktop ..."""

    # dont use "type" for variable names, as it is a reserved word
    def __init__(self, x: int, y: int, station_type: str):
        """
        Initializes a new Station instance.

        :param x: x
        :param y: y
        :param type: type
        """
        self.x = x
        self.y = y

        # self.holding will also be a string with the name of the ingredient or utensil class (lowercase) that is being held on the station.
        self.holding = ""

        self.images = {"oni": (0, 56, 48, 16, 16), "egg": (0, 88, 48, 16, 16), "cho": (0, 104, 48, 16, 16), "tom": (0, 72, 48, 16, 16), "pot": (0, 120, 48, 16, 16),
                       "brd": (0, 0, 48, 16, 16), "ble": (0, 0, 48, 16, 16), "pan": (0, 24, 48, 16, 16), "plt": (0, 0, 48, 16, 16), "srv": (0, 40, 64, 16, 16),
                       "pss": (0, 0, 64, 16, 16), "bin": (0, 24, 64, 16, 16), "snk": (0, 40, 48, 16, 16), "rtn": (0, 0, 48, 16, 16),
                       "fre": (0, 0, 48, 16, 16), "wal": (0, 0, 48, 16, 16), "": (0, 0, 112, 16, 16)}

        # self.objects = {...} -> to be completed
        
        # Defined after self.images because to validate the property, we need to check if the type is in self.images.keys()
        self.station_type = station_type
        self.image = self.images[self.station_type]


    def draw(self):
        """This method will draw the station on the screen (executed every frame)"""
        pyxel.blt(self.x, self.y, *self.image, 32)
        return self


    # ERROR HANDLING ----------------------------------------
    # Properties
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def station_type(self) -> str:
        return self.__station_type

    @property
    def holding(self) -> str:
        return self.__holding

    # Setters
    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError('x position must be an int')
        elif x < 0:
            raise ValueError('x position must be positive')
        else:
            self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError('y position must be an int')
        elif y < 0:
            raise ValueError('y position must be positive')
        else:
            self.__y = y

    @station_type.setter
    def station_type(self, station_type: str):
        if not isinstance(station_type, str):
            raise TypeError('station type must be a string')
        elif station_type not in self.images.keys():
            raise ValueError('not a valid station type')
        else:
            self.__station_type = station_type

    @holding.setter
    def holding(self, holding: str):
        if not isinstance(holding, str):
            raise TypeError('station holding must be a string')
        
        # elif holding not in self.objects.keys():
        #     raise ValueError('not a valid station holding')

        else:
            self.__holding = holding