import random

TILES = (
    ["wood"] * 4 +
    ["hay"] * 4 +
    ["sheep"] * 4 +
    ["brick"] * 3 +
    ["rock"] * 3 +
    ["desert"]
)

NUMBERS = [2, 3, 3, 4, 4, 5, 5, 6, 6,
            8, 8, 9, 9, 10, 10, 11, 11, 12]

def generate_board():
    tiles = TILES.copy()
    numbers = NUMBERS.copy()

    board = []

    random.shuffle(tiles)
    random.shuffle(numbers)

    for tile in tiles:
        if tile == "desert":
            board.append({"tile": tile, "number": None})
        else:
            board.append({"tile": tile, "number": numbers.pop()})
    return board

if __name__ == '__main__':
    print(generate_board())