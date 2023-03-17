from random import randint

from snake import Snake

class Board:
    def __init__(self):
        self.__apples = {}
        self.__snake = Snake()

    def is_valid_apple(self, row, column):

        if ((row, column) in self.__apples.keys() or
        (row, column - 1) in self.__apples.keys() or
        (row, column + 1) in self.__apples.keys() or
        (row - 1, column) in self.__apples.keys() or
        (row + 1, column) in self.__apples.keys() or
        (row, column) in self.__snake.get_snake()):
            return 0

        return 1

    def add_apple(self, board_size):
        row = randint(0, board_size-1)
        column = randint(0, board_size-1)

        while not self.is_valid_apple(row, column):
            row = randint(0, board_size-1)
            column = randint(0, board_size-1)

        self.__apples[(row, column)] = 'a'

    def add_starting_apples(self, board_size, number_of_apples):
        for i in range(0, number_of_apples):
            self.add_apple(board_size)

    def remove_apple(self, coordinates):
        del(self.__apples[coordinates])

    def add_starting_snake(self, board_size):
        self.__snake.add_new_snake(board_size)

    def add_snake_segment(self, coordinates, ate_apple):
        self.__snake.add_segment(coordinates, ate_apple)

    def get_apples(self):
        return self.__apples

    def get_snake(self):
        return self.__snake.get_snake()
