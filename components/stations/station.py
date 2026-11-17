import pyxel

class Station:
    """ This class will store a station instance, without a texture.
    It will adjust according to what type of station it is.
    Examples are cutting boards, blenders, pan, ingredient drawer, free worktop ..."""
    def __init__(self, x: int, y: int, type: str):
        """
        :param x: x
        :param y: y
        :param type: type
        """
        self.x = x
        self.y = y
        self.type = type
        self.holding = None

        self.images = {"oni": (0, 56, 48, 16, 16), "egg": (0, 88, 48, 16, 16), "cho": (0, 104, 48, 16, 16), "tom": (0, 72, 48, 16, 16), "pot": (0, 120, 48, 16, 16),
                       "brd": (0, 0, 48, 16, 16), "ble": (0, 0, 48, 16, 16), "pan": (0, 24, 48, 16, 16), "plt": (0, 0, 48, 16, 16), "srv": (0, 0, 48, 16, 16),
                       "pss": (0, 0, 64, 16, 16), "bin": (0, 24, 64, 16, 16), "snk": (0, 40, 48, 16, 16), "rtn": (0, 0, 48, 16, 16),
                       "fre": (0, 0, 48, 16, 16), "wal": (0, 0, 48, 16, 16), "": (0, 0, 0, 16, 16)}
        
        self.image = self.images[self.type]

    def draw(self):
        pyxel.blt(self.x, self.y, *self.image, 32)


    # ERROR HANDLING ----------------------------------------
    # Properties

    # Setters