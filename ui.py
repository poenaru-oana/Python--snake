from texttable import Texttable

from board import Board


class UI:
    def __init__(self):
        self.__board = Board()
        self.__board_size = 0

    def move_snake_forward(self, last_turn, number_of_squares):
        for i in range (0, number_of_squares):
            if last_turn == 'up':
                self.move_snake_up()
            elif last_turn == 'down':
                self.move_snake_down()
            elif last_turn == 'left':
                self.move_snake_left()
            elif last_turn == 'right':
                self.move_snake_right()

    def move_snake_up(self):
        apples = self.__board.get_apples()
        snake = self.__board.get_snake()
        head_row = snake[-1][0]
        head_column = snake[-1][1]
        move_coordinates = (head_row-1, head_column)
        self.is_game_over(move_coordinates)

        if move_coordinates in apples.keys():
            self.__board.add_snake_segment(move_coordinates, 1)
            self.__board.remove_apple(move_coordinates)
            self.__board.add_apple(self.__board_size)
        else:
            self.__board.add_snake_segment(move_coordinates, 0)

    def move_snake_down(self):
        apples = self.__board.get_apples()
        snake = self.__board.get_snake()
        head_row = snake[-1][0]
        head_column = snake[-1][1]
        move_coordinates = (head_row + 1, head_column)
        self.is_game_over(move_coordinates)

        if move_coordinates in apples.keys():
            self.__board.add_snake_segment(move_coordinates, 1)
            self.__board.remove_apple(move_coordinates)
            self.__board.add_apple(self.__board_size)
        else:
            self.__board.add_snake_segment(move_coordinates, 0)

    def move_snake_left(self):
        apples = self.__board.get_apples()
        snake = self.__board.get_snake()
        head_row = snake[-1][0]
        head_column = snake[-1][1]
        move_coordinates = (head_row, head_column - 1)
        self.is_game_over(move_coordinates)

        if move_coordinates in apples.keys():
            self.__board.add_snake_segment(move_coordinates, 1)
            self.__board.remove_apple(move_coordinates)
            self.__board.add_apple(self.__board_size)
        else:
            self.__board.add_snake_segment(move_coordinates, 0)

    def move_snake_right(self):
        apples = self.__board.get_apples()
        snake = self.__board.get_snake()
        head_row = snake[-1][0]
        head_column = snake[-1][1]
        move_coordinates = (head_row, head_column + 1)
        self.is_game_over(move_coordinates)

        if move_coordinates in apples.keys():
            self.__board.add_snake_segment(move_coordinates, 1)
            self.__board.remove_apple(move_coordinates)
            self.__board.add_apple(self.__board_size)
        else:
            self.__board.add_snake_segment(move_coordinates, 0)

    def is_game_over(self, head_segment_coordinates):
        snake = self.__board.get_snake()

        if head_segment_coordinates in snake[:-1]:
            raise Exception ("Game Over!")
        if (head_segment_coordinates[0] < 0 or head_segment_coordinates[0] >= self.__board_size or
            head_segment_coordinates[1] < 0 or head_segment_coordinates[1] >= self.__board_size):
            raise Exception("Game Over!")

        return 0

    def configure_row(self, row_index):
        row = []
        snake = self.__board.get_snake()
        apples = self.__board.get_apples()
        for column in range(0, self.__board_size):
            if (row_index, column) in snake:
                if (row_index, column) == snake[-1]:
                    row.append('*')
                else:
                    row.append('+')
            elif (row_index, column) in apples.keys():
                row.append('a')
            else:
                row.append(' ')

        return row

    def print_board(self):
        board = Texttable()
        for row_index in range(0, self.__board_size):
            row = self.configure_row(row_index)
            board.add_row(row)

        print(board.draw())

    def set_up_game(self, number_of_apples):
        self.__board.add_starting_snake(self.__board_size)
        self.__board.add_starting_apples(self.__board_size, number_of_apples)
        self.print_board()

    def run_game(self):
        self.__board_size = int(input('Board size: '))
        number_of_apples = int(input('Number of apples: '))
        self.set_up_game(number_of_apples)

        last_turn = None

        while True:
            command_line = input('>>> ')

            try:
                if command_line == 'up':
                    if last_turn != 'down' and last_turn != 'up':
                        self.move_snake_up()
                        self.print_board()
                    elif last_turn == 'down':
                        print('You cannot turn this way!')

                elif command_line == 'down':
                    if last_turn != 'up' and last_turn != 'down':
                        self.move_snake_down()
                        self.print_board()
                    elif last_turn == 'up':
                        print('You cannot turn this way!')

                elif command_line == 'left':
                    if last_turn != 'right' and last_turn != 'left':
                        self.move_snake_left()
                        self.print_board()
                    elif last_turn == 'right':
                        print('You cannot turn this way!')

                elif command_line == 'right':
                    if last_turn != 'left' and last_turn != 'right':
                        self.move_snake_right()
                        self.print_board()
                    elif last_turn == 'left':
                        print('You cannot turn this way!')

                if 'move' not in command_line:
                    last_turn = command_line
                else:
                    command_and_argument = command_line.split(' ')
                    if len(command_and_argument) == 1:
                        self.move_snake_forward(last_turn, 1)
                    else:
                        self.move_snake_forward(last_turn, int(command_and_argument[1]))

                    self.print_board()

            except Exception as e:
                print(e)
                break
