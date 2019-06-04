# Functions
def clear_grid():
    pass


def place_ships():
    pass


def get_target():
    pass


def fire(target):
    pass


def print_board():
    pass


def check_vic(tally):
    pass


def print_welcome():
    print("Welcome To Battle Ship")


def print_exit():
    pass


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
