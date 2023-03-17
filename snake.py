class Snake:
    def __init__(self):
        self.__snake = []

    def add_new_snake(self, board_size):
        # first element in the tuple is the row index, second is the column
        # the last element in the snake list is the head segment
        self.__snake.append((board_size//2+1, board_size//2))
        self.__snake.append((board_size//2, board_size//2))
        self.__snake.append((board_size//2-1, board_size//2))

    def add_segment(self, coordinates, ate_apple):
        self.__snake.append(coordinates)
        if not ate_apple:
            self.__snake.pop(0)

    def get_snake(self):
        return self.__snake
