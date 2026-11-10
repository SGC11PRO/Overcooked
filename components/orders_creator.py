import random
from components.service_board.order import Order
from components.service_board.timer import Timer

class OrderCreator:
    """ Creates orders every certain time. Executed on board.update()"""
    def __init__(self, main_timer: Timer):
        """
        :param total_time: Level time in seconds
        """
        # Use the game's main time (3 minutes by default)
        self.total_time = main_timer.total_seconds
        
    def update(self, board):
        """
        :param board: board
        """
        self.total_time = board.main_timer.total_seconds
        # Create first order, 3 seconds since game start
        if self.total_time == board.level_time - 3:
            # Only if the order list is empty
            if not board.order_list:
                # Choose randomly between "gazpacho", "omelette" and "eggs"
                r = random.randint(1, 3)
                if r == 1:
                    order = "gazpacho"
                elif r == 2:
                    order = "omelette"
                else:
                    order = "eggs"

                board.order_list.append(Order(order))

        # Next orders are evenly spread across the time
        # order_id variable changes evry order
        order_id = 1
        if self.total_time == board.level_time - order_id * board.level_time // 3:
            # Only if the order list has less tha maximum orders (3)
            if len(board.order_list) < 3:
                # Choose randomly between "gazpacho", "omelette" and "eggs"
                r = random.randint(1, 3)
                if r == 1:
                    order = "gazpacho"
                elif r == 2:
                    order = "omelette"
                else:
                    order = "eggs"

                order_id += 1
                board.order_list.append(Order(order))



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