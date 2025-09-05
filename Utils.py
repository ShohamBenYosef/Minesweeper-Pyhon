import datetime
import json
import os



def check_valid_int(val, max_val=None,min_val=0):
    while True:
        try:
            input_val = int(input(f"Enter {val}"))

            if min_val is not None and input_val < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and input_val > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return input_val

        except ValueError:
            print("Invalid input. Try again.")



def check_start_time():
    start = datetime.datetime.now()
    return start



def calc_game_time(start_time):
    time = datetime.datetime.now() - start_time
    return time.total_seconds()



def save_status(status, duration, board_size):
    username = input("Enter your username: ")
    save_dict = {
        "username": username,
        "status": status,
        "duration": duration,
        "board_size": board_size
    }

    if os.path.exists("./scores.json"):
        with open("./scores.json", "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(save_dict)

    with open("scores.json", "w") as f:
        json.dump(data, f, indent=2)