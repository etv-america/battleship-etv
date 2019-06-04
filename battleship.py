# Functions
def clear_grid():
    pass


def place_ships():
    pass


def get_target():
    choice = input("Where would you like to aim? (example: '2,3')")
    if len(choice) > 3:
        print("Your coordinate was invalid. Please follow the example and try again.")
        get_target()
    else:
        choice_list = choice.split(',')
        target = []
        for i in choice_list:
            target.append(int(i))
        return target



def fire(target):
    pass


def print_board():
    new_grid = []
    for i in range(16):
        new_grid.append([])
    for i, k in enumerate(new_grid):
        for a in range(16):
            new_grid[i].append(0)
    return new_grid


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
    vic = False
    while not vic:
        for player in range(2):
            plr = player + 1
            target = get_target()
            result = fire(target)
            if result is "hit":
                plrs[plr]["grid"][target[0]][target[1]] = "X"
                plrs[plr]["tally"] += 1

            elif result is "miss":
                plrs[plr]["grid"][target[0]][target[1]] = "\\"
            else:
                print("please use correct coordinates, this part of the program is unfinished")
                exit()
            vic = check_vic(plrs[plr]["tally"])
    rounds += 1

print_exit()
