class Chef:
    """Documentation..."""
    
    def __init__(self, x:int, y:int):
        """
        Init method
        :param x: x position
        :param y: y position
        """
        
        self.x = x
        self.y = y
        
        # tuple (image_bank, x, y, h_size, v_size)
        self.image = (0, 0, 0, 16, 16)
        self.has_dish = False
        
    # CHEF BEHAVIOUR ------------------------------------------
    def move(self, direction: str, board_size: tuple):
        """
        Move the chef inside the screen/area. Collissions not implemented
        :param direction: string "up", "down", "left", "right"
        :param board_size: tuple (x_size, y_size), to check screen limits
        """
        # convert direction to lowercase
        direction = direction.lower()    
        DIRECTIONS = ('left', 'right', 'up', 'down')
        # validate parameters
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        elif not isinstance(board_size, tuple) or len(board_size) != 2:
            raise TypeError('board_size must be a tuple(x_size, y_size) with exactly 2 elements')
        
        elif direction not in DIRECTIONS:
            raise ValueError('must enter a valid direction (up, down, left, right)')
        elif board_size[0] < 1 or board_size[1] < 1:
            raise ValueError('board too small for the chef to move')
        
        
        # move logic
        # self.image[3] refers to horizontal image size 
        # self.image[4] refers to vertical image size
        if direction == 'right' and self.x + self.image[3] < board_size[0]:
            self.x += 1
            
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        
        elif direction == 'down' and self.y + self.image[4] < board_size[1]:
            self.y += 1
        
        elif direction == 'up' and self.y > 0:
            self.y -= 1
    
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
    
    @image.setter
    def image(self, image: tuple):
        if not isinstance(image, tuple):
            raise TypeError('image must be a tuple')
        elif len(image) != 5:
            raise ValueError('image require 5 parameters')
        else:
            self.__image = image
            
    @has_dish.setter
    def has_dish(self, has_dish: bool):
        if not isinstance(has_dish, bool):
            raise TypeError('has_dish must be a bool')
        else:
            self.__has_dish = has_dish