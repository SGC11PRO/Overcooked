import random
from components.service_board.order import Order

class OrderCreator:
    """ Creates orders every certain time. Executed on board.update()"""    
    def __init__(self):
        self.order_id = 0

        
    def update(self, board):
        """
        :param board: board
        """
        # Set time to match game time (3 minute timer)
        self.time = board.main_timer.total_seconds
        self.frame = board.main_timer.frame_count
        
        # Create first order, 3 seconds since game start
        # Next orders are evenly spread across the time
        # self.order_id attribute changes every order
        if (self.time == board.level_time - 3  - (self.order_id * board.level_time // 4)
            and self.frame == 0):
            # Choose randomly between "gazpacho", "omelette" and "eggs"
            r = random.randint(1, 3)
            if r == 1:
                order = "gazpacho"
            elif r == 2:
                order = "omelette"
            else:
                order = "eggs"

            # local variable
            order_id = self.order_id
            self.order_id += 1
            
            board.order_list.append(Order(order, board.score, order_id))

        # Pause orders if there are more than 3 on the board (and keep them hidden)
        for i in range(len(board.order_list)):
            if i >= 3:
                board.order_list[i].timer.paused = True
            else:
                board.order_list[i].timer.paused = False




    # ERROR HANDLING ----------------------------------------
    @property
    def total_time(self) -> int:
            return self.__total_time

    @total_time.setter
    def total_time(self, total_time: int):
        if not isinstance(total_time, int):
            raise TypeError("The total time must be an int")
        elif total_time < 0:
            raise ValueError('The total time must be positive')
        else:
            self.__total_time = total_time