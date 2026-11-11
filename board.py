import pyxel

# Initial objects on the board
from components.chefs.chef import Chef
from components.floor import Floor
from components.service_board.timer import Timer
from components.service_board.order import Order
from components.service_board.score import Score
from components.ingredient import Ingredient
from components.orders_creator import OrderCreator

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
        self.size = board_size

        # Time and score
        self.fps = 60
        self.level_time = 180
        self.main_timer = Timer(self.level_time) 
        
        self.score = Score()

        # Orders
        self.order_list = []
        self.order_creator = OrderCreator()
        
        # Chefs
        self.chef1 = Chef(50, 50, 0, 16)
        self.chef2 = Chef(50, 120, 0, 32)

        # Ingredients
        self.ingredient_list = []
        NAMES = ("tomato", "onion", "potato", "egg", "chorizo")
        for name in NAMES:
            ingredient = Ingredient(name)
            self.ingredient_list.append(ingredient)


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

 
    # COMPLETE ORDERS
    # To complete an order just call board.complete_order(order_id) and it will search for the order with that id and complete it. 
    # If the order is not found, it will return False.
    def complete_order(self, order_id: int) -> bool:
        for order in self.order_list:
            if order.id == order_id:
                order.complete()
                return True
            
        return False
    
    
    # Debugging only (to complete oldes order)
    def complete_oldest_order(self) ->  bool:
        for order in self.order_list:
            if order.available:
                return self.complete_order(order.id)
        
        return False
    
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
        if pyxel.btnp(chef1_interact):
            self.chef1.interact(1)
            self.complete_oldest_order() # Debugging only
            
            # self.score.add_score(10) 
                
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
            self.chef2.interact(1)

        # Updates timer class
        self.main_timer.update(self.fps)

        # Updates chef calsses (timer)
        self.chef1.update(self.fps)
        self.chef2.update(self.fps)

        # Create orders
        self.order_creator.update(self)

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
        # Draw chefs
        self.chef1.draw()
        self.chef2.draw()
    
        # Text and UI =========================================================
        # pyxel.text(10, 8, f"Chef 1: ({self.chef1.x}, {self.chef1.y})", 7)    
        # pyxel.text(10, 18, f"Chef 2: ({self.chef2.x}, {self.chef2.y})", 7)

        # Draw timer inside the service board area
        self.main_timer.draw(self.size[0] - 40, 10, 7)
        
        # Draw score inside the service board area
        pyxel.text(self.size[0] - 40, 20, str(self.score.score), 7)

        # Draw orders inside the service board area
        for order in range(len(self.order_list)):
            if order <= 2:
                self.order_list[order].draw((order) * 40, 0)

        # Draw  chefs
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