import random
import Cell


class Board(object):

    def __init__(self, width, height, num_of_mines):
        self.width = width
        self.height = height
        self.num_of_mines = num_of_mines
        self.grid = [[Cell.Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.game_over = False


    def generate_board(self):
        self.places_mines()
        self.calculate_neighbor_mines()



    def calculate_neighbor_mines(self):

        for y in range(self.height):
            for x in range(self.width):

                if self.grid[y][x].is_mine:
                    continue

                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.grid[ny][nx].is_mine:
                                count += 1

                self.grid[y][x].neighbor_mines = count



    def places_mines(self):
        mines_placed = 0

        while mines_placed < self.num_of_mines:

            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if not self.grid[y][x].is_mine:
                self.grid[y][x].is_mine = True
                mines_placed += 1



    def reveal_cell(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("Invalid coordinate")
            return

        elif self.grid[y][x].is_visible or self.grid[y][x].is_flag:
            return

        self.grid[y][x].reveal()

        if self.grid[y][x].is_mine:
            self.game_over = True
            #self.print_board()
            #print("Game Over")
            return

        if self.grid[y][x].neighbor_mines > 0:
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                self.reveal_cell(nx, ny)



    def print_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.grid[y][x].is_visible:
                    if self.grid[y][x].is_flag:
                        print("F", end="")
                    else:
                        print("#", end="")
                elif self.grid[y][x].is_mine:
                    print("*", end="")
                elif self.grid[y][x].neighbor_mines > 0:
                    print(self.grid[y][x].neighbor_mines, end="")

                else:
                    print(" ", end="")
            print()



    def is_won(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.grid[y][x].is_visible and not self.grid[y][x].is_mine:
                    return False
        return True



    def toggle_flag(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("Invalid coordinate")
            return

        elif self.grid[y][x].is_visible:
            return

        else:
            self.grid[y][x].toggle_flag()

