class ingredient:
    """ Ingredient ... """
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if name not in ("tomato", "onion", "potato", "egg", "chorizo"):
            raise ValueError('Name must be "tomato", "onion", "potato", "egg" or "chorizo"')
        else:
            self.__name = name.lower()

    @property
    def image(self) -> tuple:
        ingredient_images = {"tomato": (0, 0, 112, 16, 16),
                             "onion":  (0, 16, 112, 16, 16),
                             "potato": (0, 32, 112, 16, 16),
                             "egg":    (0, 48, 112, 16, 16),
                             "chorizo":(0, 64, 112, 16, 16)}

        return ingredient_images[self.name]