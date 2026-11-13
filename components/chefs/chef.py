import pyxel
from components.service_board.timer import Timer

class Chef:
    """Documentation..."""
    
    def __init__(self, x: int, y: int, id: int, board):
        """
        Init method
        :param x: x position
        :param y: y position
        :param id: id of the chef (Either 0 or 1)
        """
        
        self.x = x
        self.y = y     
        self.id = id
        self.board = board

        # tuple (image_bank, x, y, h_size, v_size)
        # self.__image = (1, img_x, img_y, 14, 28)
        self.has_dish = False

        # Sprites (only the y position of each image) for each state of the chef: 
        # [0] -> down
        # [1] -> left / right
        # [2] -> walking
        # [3] -> up

        # self.state_sprites = (0, 16, 32, 48)
        self.__sprites = {
            # Every chef must be in a different row
            # Chef 1 in Row 0, Chef 2 in Row 32 ...
            
            # tuple (image_bank, x, y, h_size, v_size)
            "down": (1, 0, id * 32, 14, 28),
            "left": (1, 32, id * 32, 14, 28),
            "left_walk": (1, 16, id * 32, 14, 28),
            "right": (1, 32, id * 32, -14, 28),
            "right_walk": (1, 16, id * 32, -14, 28),
            "up": (1, 48, id * 32, 14, 28),
        }
        self.__image = self.__sprites["down"]

        # Input mapping
        if self.id == 0:
            self.__inputs = {
                "right": pyxel.KEY_RIGHT,
                "left": pyxel.KEY_LEFT,
                "up": pyxel.KEY_UP,
                "down": pyxel.KEY_DOWN,
                "interact": pyxel.KEY_RSHIFT
            }
        elif self.id == 1:
            self.__inputs = {
                "right": pyxel.KEY_D,
                "left": pyxel.KEY_A,
                "up": pyxel.KEY_W,
                "down": pyxel.KEY_S,
                "interact": pyxel.KEY_LSHIFT
            }

        
        # Animation speed
        # At 60 fps, animation_speed = 60 means 2 sprite changes per second
        # At 60 fps, animation_speed = 30 means 4 sprite changes per second (faster)
        self.animation_speed = 30
        # Acting check
        self.is_acting = False

        # Timer
        self.interaction_timer = Timer(0)
        
        
    # CHEF BEHAVIOUR ------------------------------------------
    def move(self, direction: str):
        """
        Move the chef inside the kitchen, which starts at y=32. Collissions not implemented
        :param direction: string "up", "down", "left", "right"
        """
        # convert direction to lowercase
        direction = direction.lower()    
        DIRECTIONS = ('left', 'right', 'up', 'down') 
        
        # validate parameters
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        elif direction not in DIRECTIONS:
            raise ValueError('must enter a valid direction (up, down, left, right)')
        elif self.board.size[0] < 1 or self.board.size[1] < 1:
            raise ValueError('board too small for the chef to move')
        
        
        # Movement logic
        if direction == 'right' and self.x + self.__sprites["down"][3] < self.board.size[0]:
            self.x += 1
            # Walking animation
            if self.board.main_timer.frame_count % self.animation_speed < self.animation_speed / 2:
                self.__image = self.__sprites["right"]
            else:
                self.__image = self.__sprites["right_walk"]
            
        elif direction == 'left' and self.x > 0:
            self.x -= 1
            # Walking animation
            if self.board.main_timer.frame_count % self.animation_speed < self.animation_speed / 2:
                self.__image = self.__sprites["left"]
            else:
                self.__image = self.__sprites["left_walk"]

        elif direction == 'down' and self.y + self.__sprites["down"][4] < self.board.size[1]:
            self.y += 1
            self.__image = self.__sprites["down"]

        elif direction == 'up' and self.y > 32:
            self.y -= 1
            self.__image = self.__sprites["up"]

    def stop(self, direction: str):
        """
        Stop the chef and its animation
        :param direction: string "up", "down", "left", "right"
        """
        # convert direction to lowercase
        direction = direction.lower()    
        DIRECTIONS = ('left', 'right', 'up', 'down') 
        
        # validate parameters
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        elif direction not in DIRECTIONS:
            raise ValueError('must enter a valid direction (up, down, left, right)')

        if direction == 'left':
            self.__image = self.__sprites["left"]
        elif direction == 'right':
            self.__image = self.__sprites["right"]
        
    # if time is not specified, it will be 1 second by default
    def interact(self, time: int = 1):
        """
        Perform an action
        :param time: The time the action takes
        """
        self.is_acting = True
        self.interaction_timer.frame_count = 0
        self.interaction_timer.total_seconds = time
        
    def update(self):

        # Interaction timer
        self.interaction_timer.update(self.board.fps)
        if self.interaction_timer.total_seconds == 0:
            self.is_acting = False

        # Input detection
        if pyxel.btn(self.__inputs["up"]):
            self.move('up')
        if pyxel.btn(self.__inputs["down"]):
            self.move('down')
        if pyxel.btn(self.__inputs["right"]) and not pyxel.btn(self.__inputs["left"]):
            self.move('right')
        if pyxel.btn(self.__inputs["left"]) and not pyxel.btn(self.__inputs["right"]):
            self.move('left')
        if pyxel.btnr(self.__inputs["right"]):
            self.stop('right')
        if pyxel.btnr(self.__inputs["left"]):
            self.stop('left')
        if pyxel.btnp(self.__inputs["interact"]):
            self.interact()
            self.board.complete_oldest_order() # Debugging only

    def draw(self):
        pyxel.blt(self.x, self.y, *self.image, 32)

        if self.is_acting:
            # Show text
            pyxel.text(self.x + abs(self.image[3]) // 2 - 2, self.y - 8, "!", 32)

        
    
    # ERROR HANDLING ------------------------------------------
    # properties
    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y
    
    @property
    def image(self) -> tuple:
        return self.__image
    
    @property
    def has_dish(self) -> bool:
        return self.__has_dish

    @property
    def id(self) -> int:
        return self.__id
    
    
    # setters
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
            
    @has_dish.setter
    def has_dish(self, has_dish: bool):
        if not isinstance(has_dish, bool):
            raise TypeError('has_dish must be a bool')
        else:
            self.__has_dish = has_dish

    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError('id must be an int')
        elif id != 0 and id != 1:
            raise ValueError('id must be 0 or 1')
        else:
            self.__id = id