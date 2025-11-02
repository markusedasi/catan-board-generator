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

LAYOUT = [3, 4 , 5, 4, 3]

def generate_board():
    tiles = TILES.copy()
    numbers = NUMBERS.copy()

    result = []

    random.shuffle(tiles)
    random.shuffle(numbers)

    for tile in tiles:
        if tile == "desert":
            result.append({"tile": tile, "number": None})
        else:
            result.append({"tile": tile, "number": numbers.pop()})
    return result

def structure_board(tile_set):
    board_layout = LAYOUT.copy()
    result = []
    index = 0

    for number_of_tiles in board_layout:
        row = tile_set[index:index + number_of_tiles]
        result.append(row)
        index += number_of_tiles
    return result

if __name__ == '__main__':
    board = generate_board()
    structured = structure_board(board)

    print(board)
    print(structured)