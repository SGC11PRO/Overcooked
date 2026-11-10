import pyxel
from .timer import Timer

class Order:
    """ Order ... """
    def __init__(self, order: str):
        """
        Possible orders:
        Gazpacho: 45 seconds, 10 points, -5 if lost; chopped tomato + chopped onion + blender
        Spanish omelette: 60s, 12p, -6p if lost; chopped potato + chopped onion + egg + pan
        Eggs with chorizo: 60s, 12p, -6p if lost; chopped potato + chopped chorizo + egg + pan

        :param order: The order: "gazpacho", "omelette" or "eggs"
        :param x: x position
        :param y: y position
        """

        self.order = order
        # tuple (image_bank, x, y, h_size, v_size)
        self.bg_image = (0, 0, 80, 40, 24)

        # Change time, points and sprite depending on the order
        if order == "gazpacho":
            self.time = 45
            self.points_if_ok = 10
            self.points_if_lost = -5
            self.image = (0, 32, 0, 16, 16)
        elif order == "omelette":
            self.time = 60
            self.points_if_ok = 12
            self.points_if_lost = -6
            self.image = (0, 16, 0, 16, 16)
        else:
            self.time = 60
            self.points_if_ok = 12
            self.points_if_lost = -6
            self.image = (0, 32, 0, 16, 16)

        # Add a timer
        self.timer = Timer(self.time)
        self.frame_count = 0

        # Availability (Not available if time is over)
        self.available = True

    def draw(self, x: int, y: int):
        if not isinstance(x, int):
            raise TypeError('x position must be an int')
        elif x < 0:
            raise ValueError('x position must be positive')

        if not isinstance(y, int):
            raise TypeError('y position must be an int')
        elif y < 0:
            raise ValueError('y position must be positive')

        # Draw background, plate and timer
        pyxel.blt(x, y, *self.bg_image, 32)
        pyxel.blt(x + 2, y, *self.image, 32)
        self.timer.draw(x + 20, y + 5, 7)

    def update(self, fps: int):
        """
        :param fps: frames per second
        """
        self.frame_count += 1
        if self.frame_count >= fps:
            self.timer.decrease(1)
            self.frame_count = 0

        if self.timer.total_seconds == 0:
            self.lost()
    

    def lost(self):
        self.available = False
            

        

    # ERROR HANDLING -----------------------------------------
    # Properties
    @property
    def order(self) -> str:
        return self.__order

    # Setters
    @order.setter
    def order(self, order: str):
        if not isinstance(order, str):
            raise TypeError("The order must be a string")
        elif not order:
            raise ValueError("The order can't be empty")
        elif order.lower() not in ("gazpacho", "omelette", "eggs"):
            raise ValueError('Order must be "gazpacho", "omelette" or "eggs"')
        else:
            self.__order = order.lower()