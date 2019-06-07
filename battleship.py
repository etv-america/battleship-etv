# imports

import random

import pygame

pygame.mixer.init()


# sounds


def hit_music():
    pygame.mixer.music.load('hardcore.mp3')
    pygame.mixer.music.play()


def miss_music():
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()


def skip_music():
    pygame.mixer.music.load('fricks.mp3')
    pygame.mixer.music.play(1)


def hit_sound():
    sound = pygame.mixer.Sound('388528__eflexmusic__artillery-explosion-close-mixed.wav')
    sound.play()


def miss_sound():
    sound = pygame.mixer.Sound('9508__petenice__splash.wav')
    sound.play()


# Functions


def retrieve_size():  # Asks user for a difficulty and outputs length of one side of the grid
    difficulty = input("Enter difficulty: 1, 2, or 3. \n")
    if difficulty == "1":
        return 8
    elif difficulty == "2":
        return 16
    elif difficulty == "3":
        return 32
    else:
        print("Invalid difficulty! Try again. \n")
        return 0


def clear_grid():  # Produces empty grid in the size chosen by user
    new_grid = []
    for i in range(grid_size):
        new_grid.append([])
    for i, k in enumerate(new_grid):
        for a in range(grid_size):
            new_grid[i].append("-")
    return new_grid


def check_ships(ask, ships):  # Checks whether it's safe to place a ship in the coordinate ask
    if ask == [-1, -1]:
        return True
    elif ask in ships:
        return False
    else:
        return True


def place_ships():  # Randomly places ships and outputs list of ship coordinates.\
    # There is a length 5, 4, 3, and 2, making a total of four ships
    ships = []
    for i in range(4):
        collision = True
        while collision:
            check_collision = 0
            length = i + 2
            valid_ship = []
            direction = random.randint(1, 2)  # 1 = vertical, 2 = horizontal
            if direction == 1:
                third = [-1, -1]
                fourth = [-1, -1]
                fifth = [-1, -1]
                first = [random.randint(1, (grid_size - length + 1)), random.randint(1, grid_size)]
                second = [first[0] + 1, first[1]]
                if length >= 3:
                    third = [first[0] + 2, first[1]]
                    if length >= 4:
                        fourth = [first[0] + 3, first[1]]
                        if length >= 5:
                            fifth = [first[0] + 4, first[1]]
            else:
                third = [-1, -1]
                fourth = [-1, -1]
                fifth = [-1, -1]
                first = [random.randint(1, grid_size), random.randint(1, (grid_size - length + 1))]
                second = [first[0], first[1] + 1]
                if length >= 3:
                    third = [first[0], first[1] + 2]
                    if length >= 4:
                        fourth = [first[0], first[1] + 3]
                        if length >= 5:
                            fifth = [first[0], first[1] + 4]
            new_ship = [first, second, third, fourth, fifth]
            for k in new_ship:
                if check_ships(k, ships):
                    valid_ship.append(k)
                else:
                    check_collision += 1
            if check_collision == 0:
                ships.extend(valid_ship)
                collision = False
    return ships


def get_target():  # Asks player for a target and determines validity of target
    choice = input("\nWhere would you like to aim? (example: '12,3') \n")
    try:
        int(choice)
    except ValueError:
        if not (choice.split(','))[0].isdigit() or not (choice.split(','))[1].isdigit() \
                or not 1 <= int((choice.split(','))[0]) <= grid_size \
                or not 1 <= int((choice.split(','))[1]) <= grid_size \
                or len(choice.split(',')) > 2:
            target = 0
            print("Invalid coordinate. Please try again.")
            return target
        else:
            choice_list = choice.split(',')
            target = []
            for i in choice_list:
                target.append(int(i))
            target = [target[1], target[0]]
            return target
    else:
        print("You need TWO numbers. Try again.")
        return 0


def check_availability(target, grid):  # Checks whether a space has already been hit
    if grid[(target[0] - 1)][(target[1] - 1)] == "-":
        return True
    else:
        return False


def check_hit(target, ships):  # Checks to see if target hits a ship
    if target in plrs[plr]["ships"]:
        return True
    else:
        return False


def fire(target, grid, ships):  # Uses target, grid, and ships to determine the outcome of the player's input
    if check_availability(target, grid):
        if check_hit(target, ships):
            return "hit"
        else:
            return "miss"
    else:
        return "skip"


def print_board(grid):  # Prints the current board including '-'s, 'X's, and '/'s
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
        grid_print = string
        print(grid_print)
    print("\n")


def check_vic(tally):  # Checks whether a player has sunk every ship or not
    if tally >= 14:
        print("Player " + str(plr) + " won!")
        print_exit()
        return True
    else:
        return False


def print_welcome():  # Asks the user whether they will play
    print("Welcome To Battle Ship! The game of luck and strategy. \n")
    response = input("Would you like to play a game? Y/N \n")
    if response[0] is "N" or response[0] is "n":
        exit()


def print_exit():  # Exits the game
    print("\nThanks for playing!")
    exit()


# Main Loop
grid_size = 0

print_welcome()

while grid_size == 0:
    grid_size = retrieve_size()

plrs = {
    1: {
        "grid": [],
        "ships": {

        },
        "tally": 0,
        "targets": [],
        "score": 0,
        "last": "hit"
    },

    2: {
        "grid": [],
        "ships": {

        },
        "tally": 0,
        "targets": [],
        "score": 0,
        "last": "hit"
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
            if plrs[1]["last"] == "hit" or plrs[2]["last"] == "hit":
                hit_music()
            elif plrs[plr]["last"] == "skip":
                skip_music()
            else:
                miss_music()
            print("\n It's " + str(plr) + "'s turn! \n")
            print_board(plrs[plr]["grid"])
            target = 0
            while target == 0:
                target = get_target()
            result = fire(target, plrs[plr]["grid"], plrs[plr]["ships"])
            if result is "hit":
                hit_sound()
                plrs[plr]["grid"][target[0] - 1][target[1] - 1] = "X"
                plrs[plr]["tally"] += 1
                print_board(plrs[plr]["grid"])
                print("\nXXXXXXXXXXXXXXX\n    Hit!!!!    \nXXXXXXXXXXXXXXX\n")
                plrs[plr]["last"] = "hit"

            elif result is "miss":
                miss_sound()
                plrs[plr]["grid"][target[0] - 1][target[1] - 1] = "/"
                print_board(plrs[plr]["grid"])
                print("\n///////////////\n    Miss :(    \n///////////////\n")
                plrs[plr]["last"] = "miss"

            elif result is "skip":
                print("\nWhen will you learn that YOUR ACTIONS HAVE CONSEQUENCES?! \
                 \nYou Have Been Skipped. Weep, Fool. \n \n")
                plrs[plr]["last"] = "skip"

            else:
                print("please use correct coordinates, this part of the program is unfinished")
                exit()
            vic = check_vic(plrs[plr]["tally"])
    rounds += 1

print_exit()
