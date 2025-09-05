import Board
import Utils

def game_over(start_time, status, board_size):
    time = Utils.calc_game_time(start_time)
    print(time)
    Utils.save_status(status, time, board_size)
    print(f"Game Over, you {status}!")



def game():
    width = Utils.check_valid_int("width")
    height = Utils.check_valid_int("height")
    num_of_mines = Utils.check_valid_int("number of mines:")

    board = Board.Board(width, height, num_of_mines)
    board.generate_board()

    start_time = Utils.check_start_time()
    while not board.game_over:
        board.print_board()
        action = input("Enter action: flag / open / exit")

        x = Utils.check_valid_int("x")
        y = Utils.check_valid_int("y")

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
            game_over(start_time, "Win")

    if board.game_over:
        game_over(start_time, "Lose", f"{width}x{height}")

if __name__ == '__main__':
    print("Welcome to Minesweeper!")
    game()
