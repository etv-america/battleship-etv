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


def win_sound():
    sound = pygame.mixer.Sound('Applause-SoundBible.com-151138312.wav')
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
    else:
        for n in range(5 * double):
            if ask in ships["ship " + str(n + 1)]:
                return False
        return True


def place_ships():  # Randomly places ships and outputs list of ship coordinates.\
    # There is a length 5, 4, 3, and 2, making a total of four ships
    ships = {}
    for s in range(double * 5):
        ships.update({"ship " + str(s + 1): []})
    for q in range(double):
        for i in range(5):
            collision = True
            while collision:
                check_collision = 0
                if i >= 2:
                    length = i + 1
                else:
                    length = i + 2
                valid_ship = []
                third = [-1, -1]
                fourth = [-1, -1]
                fifth = [-1, -1]
                direction = random.randint(1, 2)  # 1 = vertical, 2 = horizontal
                first = [random.randint(1, (grid_size - length + 1)), random.randint(1, grid_size)]
                second = [first[0] + 1, first[1]]
                if length >= 3:
                    third = [first[0] + 2, first[1]]
                    if length >= 4:
                        fourth = [first[0] + 3, first[1]]
                        if length >= 5:
                            fifth = [first[0] + 4, first[1]]
                new_ship = [first, second, third, fourth, fifth]
                if direction == 2:
                    for m in range(5):
                        new_ship[m] = [new_ship[m][1], new_ship[m][0]]
                for k in new_ship:
                    if check_ships(k, ships):
                        valid_ship.append(k)
                    else:
                        check_collision += 1
                if check_collision == 0:
                    valid_ship = {"ship " + str(5 * q + (i + 1)): valid_ship}
                    ships.update(valid_ship)
                    collision = False
    for l in range(5 * double):
        empty = True
        while empty:
            if [-1, -1] in ships["ship " + str(l + 1)]:
                ships["ship " + str(l + 1)].remove([-1, -1])
            else:
                empty = False
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
    for i in range(5 * double):
        i = i + 1
        if target in ships["ship " + str(i)]:
            print("\nXXXXXXXXXXXXXXX\n    Hit!!!!    \nXXXXXXXXXXXXXXX\n")
            ships["ship " + str(i)].remove(target)
            if ships["ship " + str(i)] == []:
                if i % 5 == 4:
                    print("\nOOOOOOOOOOOOOOOOOOOOOOO\nYou sunk the Battleship!!!\nOOOOOOOOOOOOOOOOOOOOOOO\n\n")
                if i % 5 == 0:
                    print("\nOOOOOOOOOOOOOOOOOOOO\nYou sunk the Carrier!!!\nOOOOOOOOOOOOOOOOOOOO\n\n")
                if i % 5 == 1:
                    print("\nOOOOOOOOOOOOOOOOOOOOOO\nYou sunk the Destroyer!!!\nOOOOOOOOOOOOOOOOOOOOOO\n\n")
                if i % 5 == 2:
                    print("\nOOOOOOOOOOOOOOOOOOOOOO\nYou sunk the Submarine!!!\nOOOOOOOOOOOOOOOOOOOOOO\n\n")
                if i % 5 == 3:
                    print("\nOOOOOOOOOOOOOOOOOOOO\nYou sunk the Cruiser!!!\nOOOOOOOOOOOOOOOOOOOO\n\n")
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
    if tally >= 17 * double:
        print("Player " + str(plr) + " won!\n")
        win_sound()
        print_exit()
        input("Any last words?\n")
        return True
    else:
        return False


def print_welcome():  # Asks the user whether they will play
    players = 0
    print("Welcome To Battle Ship! The game of luck and strategy. \n")
    response = input("Would you like to play a game? Y/N \n")
    if response[0] is "N" or response[0] is "n":
        exit()
    while players == 0:
        ask = input("How many players will play? (2 at most)\n")
        if ask == "1":
            players = 1
        elif ask == "2":
            players = 2
        elif ask == "0":
            print("Oh. okay. Bye, I guess.")
            exit()
        else:
            print("That isn't a valid number of players! Try again.")
    return players


def print_exit():  # Exits the game
    print("\nThanks for playing!")
    exit()


# Main Loop
grid_size = 0

game_mode = print_welcome()

while grid_size == 0:
    grid_size = retrieve_size()

if grid_size >= 32:
    double = 4
else:
    double = 1

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
        for player in range(game_mode):
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
            if game_mode == 1:
                print("It's Computer's turn!")
                if grid_size == 8:
                    chance = 5
                elif grid_size == 16:
                    chance = 14
                else:
                    chance = 11
                guess = random.randint(1, chance)
                if guess == 1:
                    plrs[2]["tally"] += 1
                    print("\nXXXXXXXXXXXXXXX\n    Hit!!!!    \nXXXXXXXXXXXXXXX\n")
                else:
                    print("\n///////////////\n    Miss :(    \n///////////////\n")
                if plrs[2]["tally"] >= double * 17:
                    print("\n------------------------------\nLmao the computer beat you. \
                    Cya nerd.\n------------------------------")
                    exit()
    rounds += 1

print_exit()
