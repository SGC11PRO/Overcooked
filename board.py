import pyxel

# Initial objects on the board
from components.chefs.chef import Chef
from components.floor import Floor
from components.service_board.timer import Timer

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
        self.board_size = board_size

        # Service board size (width, Creatingheight -> fixed to 32px)
        self.service_board_size = (board_size[0], 32)

        # fps
        self.fps = 60
        self.frame_count = 0

        # Create timer obj (seconds)
        self.main_timer = Timer(180) 
        
        # Create chef objs
        # 2 chef styles (img_x) -> 0, 16 or 32, 48
        self.chef1 = Chef(96, 136, 16, 16)
        self.chef2 = Chef(96, 136, 32, 16)

        # Setup pyxel environment
        pyxel.init(
            self.board_size[0], 
            self.board_size[1], 
            title='Overcooked', 
            fps=self.fps, 
            quit_key=pyxel.KEY_ESCAPE, 
            display_scale=4)

        pyxel.load('assets/overcooked.pyxres')
        pyxel.run(self.update, self.draw)
    
    # BOARD LOGIC ------------------------------------------
    def update(self):
        """Executed in every frame. Logic to exit the game is already defined
        in pyxel.init(quit_key=pyxel.KEY_ESCAPE)"""
        
        # Update chef position every frame
        # chef 1 (arrows)
        if pyxel.btn(chef1_right):
            self.chef1.move('right', self.board_size)
        if pyxel.btn(chef1_left):
            self.chef1.move('left', self.board_size)
        if pyxel.btn(chef1_up):
            self.chef1.move('up', self.board_size)
        if pyxel.btn(chef1_down):
            self.chef1.move('down', self.board_size)
            
        # chef 2 (WASD)
        if pyxel.btn(chef2_right):
            self.chef2.move('right', self.board_size)
        if pyxel.btn(chef2_left):
            self.chef2.move('left', self.board_size)
        if pyxel.btn(chef2_up):
            self.chef2.move('up', self.board_size)
        if pyxel.btn(chef2_down):
            self.chef2.move('down', self.board_size)

        # Update timer every frame
        self.frame_count += 1
        if self.frame_count == self.fps:
            self.main_timer.decrease(1)
            self.frame_count = 0
            
    def draw(self):
        """Executed in every frame. Logic to draw sprites on the screen"""
        # erasing previous screen
        pyxel.cls(0)


        # [!] Important to draw the floor before everything else, so the rest of elements
        # are rendered above the floor tiles, and not behind

        # Draw floor on every tile based on boarsize
        # step=16 since sprites are 16x16 sized, so they dont overlap
        for y_tile in range(self.service_board_size[1], self.board_size[1], 16):
            for x_tile in range(0, self.board_size[0], 16):
                # create floor obj on each tile
                floor = Floor(x_tile, y_tile)

                # draw floor
                pyxel.blt(floor.x, floor.y, *floor.image)
        
        # drawing chefs -> colkey sets the transparent color by entering the color index on the palette (32 -> black)
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image, colkey=32)
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image, colkey=32)
    
        
        # text position -> pyxel.text(x, y, text, color)
        pyxel.text(10, 8, f"({self.chef1.x}, {self.chef1.y})", 7)    
        pyxel.text(10, 18, f"({self.chef2.x}, {self.chef2.y})", 7)

        # draw timer
        self.main_timer.draw_timer(self.service_board_size[0] - 30, 10, 7)

    
    # ERROR HANDLING ---------------------------------------
    # properties
    @property
    def size(self) -> tuple:
        return self.__size
    
    # setters
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