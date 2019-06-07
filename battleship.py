# Functions
def retrieve_size():
    difficulty = input("Enter difficulty: 1, 2, or 3.")
    if difficulty == "1":
        return 16
    elif difficulty == "2":
        return 32
    elif difficulty == "3":
        return 64
    else:
        print("Invalid difficulty! Try again.")
        retrieve_size()


def clear_grid():
    new_grid = []
    for i in range(grid_size):
        new_grid.append([])
    for i, k in enumerate(new_grid):
        for a in range(grid_size):
            new_grid[i].append("0")
    return new_grid


def place_ships():
    ships = {
        "carrier": [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
        "cruiser": [[2, 4], [3, 4], [4, 4]]
    }
    return ships


def get_target():
    choice = input("Where would you like to aim? (example: '12,3')")
    if not (choice.split(','))[0].isdigit() or not (choice.split(','))[1].isdigit() \
            or 1 <= int((choice.split(','))[0]) > grid_size or 1 <= int((choice.split(','))[1]) > grid_size:
        print("Your coordinate was invalid. Please follow the example and try again.")
        get_target()
    else:
        choice_list = choice.split(',')
        target = []
        for i in choice_list:
            target.append(int(i))
        target = [target[1], target[0]]
        return target


def check_availability(target, grid):
    if grid[(target[0] - 1)][(target[1] - 1)] == "0":
        return True
    else:
        return False


def check_hit(target, ships):
    if target in ships["carrier"] or target in ships["cruiser"]:
        return True
    else:
        return False


def fire(target, grid):
    if check_availability(target, grid):
        if check_hit(target, grid):
            return "hit"
        else:
            return "miss"
    else:
        return "retry"


def print_board(grid):
    side_len = grid_size  # one side of the grid matrix
    coord_a = "    "  # first line of board
    spacer = "  "  # space between grid locations
    for a in range(side_len):
        coord_a = coord_a + str(a + 1) + " " * (3 - len(str(a + 1)))  # implements letters into first line
    print(coord_a)
    for i in range(side_len):  # begins to separate grid into individual strings
        string = str(i + 1) + spacer
        if i < 9:
            string = " " + string
        for k in range(side_len):
            string = string + grid[i][k] + spacer
        grid[i] = string
        print(grid[i])


def check_vic(tally):
    if tally >= 17:
        print("Player " + str(plr) + " won!")
        return True
    else:
        return False


def print_welcome():
    print("Welcome To Battle Ship! The game of luck and strategy.")
    response = input("Would you like to play a game? Y/N")
    if response is "N":
        exit()


def print_exit():
    print("Thanks for playing!")


# Main Loop

print_welcome()

grid_size = retrieve_size()

plrs = {
    1: {
        "grid": [],
        "ships": {

        },
        "tally": 0,
        "targets": [],
        "score": 0
    },

    2: {
        "grid": [],
        "ships": {

        },
        "tally": 0,
        "targets": [],
        "score": 0
    }
}

rounds = 0
vic = False
while rounds <= 3:
    plrs[1]["grid"] = clear_grid()
    plrs[2]["grid"] = clear_grid()
    plrs[1]["ships"] = place_ships()
    plrs[2]["ships"] = place_ships()
    plrs[1]["tally"] = 0
    plrs[2]["tally"] = 0
    vic = False
    while not vic:
        for player in range(2):
            plr = player + 1
            target = get_target()
            result = fire(target, plrs[plr]["grid"])
            if result is "hit":
                plrs[plr]["grid"][target[0]][target[1]] = "X"
                plrs[plr]["tally"] += 1

            elif result is "miss":
                plrs[plr]["grid"][target[0]][target[1]] = "/"

            else:
                print("please use correct coordinates, this part of the program is unfinished")
                exit()
            vic = check_vic(plrs[plr]["tally"])
    rounds += 1

print_exit()
