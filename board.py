import pyxel

# Initial objects on the board
from components.chefs.chef import Chef
from components.service_board.timer import Timer
from components.service_board.score import Score
from components.floor import Floor
from components.ingredient import Ingredient
from components.orders_creator import OrderCreator

class Board:
    """This class contain all the logic of the game, and will be the main class that will be executed by pyxel."""
    """This class contain all the logic of the game, and will be the main class that will be executed by pyxel."""
    
    def __init__(self, board_size: tuple):
        """
        Initializes a new Board instance.
        Initializes a new Board instance.
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
        self.chef1 = Chef(50, 40, 0, self)
        self.chef2 = Chef(50, 120, 1, self)

        # Ingredients
        self.ingredient_list = []
        NAMES = ("tomato", "onion", "potato", "egg", "chorizo")
        for name in NAMES:
            ingredient = Ingredient(name)
            self.ingredient_list.append(ingredient)

        self.floor = Floor()

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
        """This method will complete an order with the given id. It will call the order class and execute .complete() method.
        :returns: True if the order is found and completed, False otherwise."""

        """This method will complete an order with the given id. It will call the order class and execute .complete() method.
        :returns: True if the order is found and completed, False otherwise."""

        for order in self.order_list:
            if order.id == order_id:
                order.complete()
                return True
            
        return False


    # Debugging only (to complete oldes order)
    def complete_oldest_order(self) ->  bool:
        """
        ONLY FOR DEBUGGING PURPOSES

        This method will complete the oldest order in the order list. It will call the order class and execute .complete() method.
        :returns: True if the order is found and completed, False otherwise."""

        for order in self.order_list:
            if order.available:
                return self.complete_order(order.id)
        
        return False

    # BOARD LOGIC ------------------------------------------
    def __draw_chefs_before_row(self, row: int, drawn_chefs: list):
        """Draw chefs that are behind the stations in this row."""
        row_bottom = 32 + 16 * row + 16

        # If the chef is above the bottom of the row (meaning that the chef is behind the stations in this row), draw the chef first
        for chef in (self.chef1, self.chef2):
            if chef not in drawn_chefs and chef.y + 28 <= row_bottom:
                chef.draw()
                drawn_chefs.append(chef)

    def update(self):
        """Executed in every frame."""

        # Updates timer class
        self.main_timer.update(self.fps)

        # Updates chefs
        self.chef1.update(self)
        self.chef2.update(self)

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
        # Draw rows and chefs from back to front.
        drawn_chefs = []
        for row in range(len(self.floor.layout)):
            self.__draw_chefs_before_row(row, drawn_chefs)

            # draw the rows after drawing the chefs that are behind the stations in this row
            self.floor.draw(row)

        # The chefs that are not in drawn_chefs are in front of all the stations, so we draw them now (after the stations)
        for chef in (self.chef1, self.chef2):
            if chef not in drawn_chefs:
                chef.draw()



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