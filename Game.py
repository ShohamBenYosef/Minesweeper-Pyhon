import Board


def game_over():
    print("Game Over - Looser")

def game():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    num_of_mines = int(input("Enter number of mines: "))
    # TODO check num of mine < widht * height

    board = Board.Board(width, height, num_of_mines)
    board.generate_board()


    while not board.game_over:
        board.print_board()
        action = input("Enter action: flag / open / exit")

        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))

        if action == "exit":
            board.game_over = True
            break

        elif action == "flag":
            board.toggle_flag(x, y)

        elif action == "open":
            board.reveal_cell(x, y)

        else:
            continue

        if board.is_won():
            print("🎉 You won!")
            board.game_over = True

    if board.game_over:
        game_over()

if __name__ == '__main__':

    print("Welcome to Minesweeper!")

    game()
