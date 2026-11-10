import pyxel

# Initial objects on the board
from components.chefs.chef import Chef
from components.floor import Floor
from components.service_board.timer import Timer
from components.service_board.order import Order

# Input mapping
chef1_right = pyxel.KEY_RIGHT
chef1_left = pyxel.KEY_LEFT
chef1_up = pyxel.KEY_UP
chef1_down = pyxel.KEY_DOWN
chef1_interact = pyxel.KEY_RSHIFT

chef2_right = pyxel.KEY_D
chef2_left = pyxel.KEY_A
chef2_up = pyxel.KEY_W
chef2_down = pyxel.KEY_S
chef2_interact = pyxel.KEY_LSHIFT


class Board:
    """Documentation..."""
    
    def __init__(self, board_size: tuple):
        """
        Documentation...
        :param board_size: Tuple (width, height) for board
        """
        # board size
        self.size = board_size
        
        # fps
        self.fps = 60

        # Create timer obj (seconds)
        self.main_timer = Timer(180) 

        # Create test orders
        self.order_list = []
        self.order_list.append(Order("gazpacho"))
        
        # Create chef objs
        self.chef1 = Chef(50, 50, 0, 16)
        self.chef2 = Chef(50, 120, 0, 32)

        # Setup pyxel environment
        pyxel.init(
            self.size[0], 
            self.size[1], 
            title='Overcooked', 
            fps=self.fps, 
            quit_key=pyxel.KEY_ESCAPE, 
            display_scale=4)

        pyxel.load('assets/overcooked.pyxres')
        pyxel.run(self.update, self.draw)

    # BOARD LOGIC ------------------------------------------
    def update(self):
        """Executed in every frame."""
        
        # Chef 1 controls (arrows)
        if pyxel.btn(chef1_right):
            self.chef1.move('right', self)
        if pyxel.btn(chef1_left):
            self.chef1.move('left', self)
        if pyxel.btn(chef1_up):
            self.chef1.move('up', self)
        if pyxel.btn(chef1_down):
            self.chef1.move('down', self)
        if pyxel.btn(chef1_interact):
            self.chef1.interact(5)    
                
        # Chef 2 controls (WASD)
        if pyxel.btn(chef2_right):
            self.chef2.move('right', self)
        if pyxel.btn(chef2_left):
            self.chef2.move('left', self)
        if pyxel.btn(chef2_up):
            self.chef2.move('up', self)
        if pyxel.btn(chef2_down):
            self.chef2.move('down', self)
        if pyxel.btn(chef2_interact):
            self.chef2.interact(5)

        # Updates timer class
        self.main_timer.update(self.fps)

        # Updates chef calsses
        self.chef1.update(self.fps)
        self.chef2.update(self.fps)

        # Updates order class (Iterating through a shallow copy)
        for order in self.order_list[:]:
            # Update all orders
            order.update(self.fps)
            # Deletes unavailable orders (done or time's over)
            if not order.available:
                self.order_list.remove(order)
        
            
    def draw(self):
        """Executed in every frame. Logic to draw sprites on the screen"""
        # Erasing previous screen
        pyxel.cls(0)


        # Draw scene using tilemaps ==========================================

        # pyxel.bltm(x, y, tm, u, v, w, h, [colkey])
        # x, y -> Position of tilemap on the screen (in pixels)
        # tm -> tilemap bank (0-2) where the tilemap is stored
        # u, v -> tile coordinates where the tilemap starts 
        # w, h -> Width and height of the tilemap to draw 

        # draw tilemap for kitchen + service board
        pyxel.bltm(0, 0, 0, 0, 0, self.size[0], self.size[1], colkey=32)


        # Objects ==========================================
        # Draw chefs (colkey=32 to set transparency)
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image, colkey=32)
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image, colkey=32)
    
        # Text and UI =========================================================
        pyxel.text(10, 8, f"Chef 1: ({self.chef1.x}, {self.chef1.y})", 7)    
        pyxel.text(10, 18, f"Chef 2: ({self.chef2.x}, {self.chef2.y})", 7)

        # Draw timer inside the service board area
        self.main_timer.draw(self.size[0] - 40, 10, 7)

        # Draw orders inside the service board area
        if self.order_list:
            self.order_list[0].draw(80, 0)

        # Draw interact actions for chefs
        self.chef1.draw()
        self.chef2.draw()

    # ERROR HANDLING ---------------------------------------
    @property
    def size(self) -> tuple:
        return self.__size
    
    @size.setter
    def size(self, size: tuple):
        if not isinstance(size, tuple) or len(size) != 2:
            raise TypeError('board size must be a tuple of length 2')
        elif not all(isinstance(i, int) for i in size):
            raise TypeError('board size must be a tuple of integers')
        elif not all(i > 0 for i in size):
            raise ValueError('board size must be a tuple of positive integers')
        else:
            self.__size = size