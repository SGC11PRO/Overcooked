import pyxel
from components.service_board.timer import Timer

class Chef:
    """Documentation..."""
    
    def __init__(self, x:int, y:int, img_x:int=0, img_y:int=0):
        """
        Init method
        :param x: x position
        :param y: y position
        :param img_x: x position of the image in the image bank
        :param img_y: y position of the image in the image bank
        """
        
        self.x = x
        self.y = y

        self.img_x = img_x
        self.img_y = img_y
        
        
        # tuple (image_bank, x, y, h_size, v_size)
        self.__image = (0, img_x, img_y, 16, 16)
        self.has_dish = False

        # Sprites (only the y position of each image) for each state of the chef: 
        # [0] -> down
        # [1] -> up
        # [2] -> right
        # [3] -> left

        self.state_sprites = (0, 16, 32, 48)

        # Acting check
        self.is_acting = False

        # Timer and frame counter
        self.frame_count = 0
        self.timer = Timer(0)
        
        
    # CHEF BEHAVIOUR ------------------------------------------
    def move(self, direction: str, board):
        """
        Move the chef inside the kitchen, which starts at y=32. Collissions not implemented
        :param direction: string "up", "down", "left", "right"
        :param board: Board object to get the size of the board
        """
        # convert direction to lowercase
        direction = direction.lower()    
        DIRECTIONS = ('left', 'right', 'up', 'down') 
        
        # validate parameters
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        elif direction not in DIRECTIONS:
            raise ValueError('must enter a valid direction (up, down, left, right)')
        elif board.size[0] < 1 or board.size[1] < 1:
            raise ValueError('board too small for the chef to move')
        
        
        # move logic
        # self.image[3] refers to horizontal image size 
        # self.image[4] refers to vertical image size
        if direction == 'right' and self.x + self.image[3] < board.size[0]:
            self.x += 1
            self.__image = (0, self.state_sprites[2], self.img_y, 16, 16)
            
        elif direction == 'left' and self.x > 0:
            self.x -= 1
            self.__image = (0, self.state_sprites[3], self.img_y, 16, 16)

        elif direction == 'down' and self.y + self.image[4] < board.size[1]:
            self.y += 1
            self.__image = (0, self.state_sprites[0], self.img_y, 16, 16)

        elif direction == 'up' and self.y > 32:
            self.y -= 1
            self.__image = (0, self.state_sprites[1], self.img_y, 16, 16)


    def interact(self, time: int):
        """
        Perform an action
        :param time: The time the action takes
        """
        self.is_acting = True
        self.timer.total_seconds = time
        
    def update(self, fps: int):
        """
        :param fps: frames per second
        """
        self.timer.update(fps)
        
        if self.timer.total_seconds == 0:
            self.is_acting = False

    def draw(self):
        if self.is_acting:
            # Show text
            pyxel.text(self.x, self.y - 8, "Action", 32)

        
    
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