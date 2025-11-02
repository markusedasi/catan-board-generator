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
    return avoid_adjacent_duplicates(result)

def structure_board(tile_set):
    board_layout = LAYOUT.copy()
    result = []
    index = 0

    for number_of_tiles in board_layout:
        row = tile_set[index:index + number_of_tiles]
        result.append(row)
        index += number_of_tiles
    return result

def avoid_adjacent_duplicates(tile_set):
    numbers = NUMBERS.copy()
    random.shuffle(numbers)

    structured_board = []
    available_tiles = tile_set.copy()

    for row_size in LAYOUT:
        board_row = []

        for col_index in range(row_size):
            placed = False

            for tile_index, tile_obj in enumerate(available_tiles):
                left_ok = (col_index == 0 or tile_obj["tile"] != board_row[col_index - 1]["tile"])

                above_ok = True
                if structured_board:
                    previous_row = structured_board[-1]
                    offsets = [col_index - 1, col_index]
                    for offset in offsets:
                        if 0 <= offset < len(previous_row):
                            if previous_row[offset]["tile"] == tile_obj["tile"]:
                                above_ok = False
                                break

                if left_ok and above_ok:
                    if tile_obj["tile"] != "desert" and numbers:
                        tile_obj["number"] = numbers.pop()
                    board_row.append(tile_obj)
                    available_tiles.pop(tile_index)
                    placed = True
                    break

            if not placed:
                return generate_board()

        structured_board.append(board_row)

    flat_board = []
    for row in structured_board:
        for tile_obj in row:
            flat_board.append(tile_obj)

    return flat_board


if __name__ == '__main__':
    board = generate_board()
    structured = structure_board(board)

    print(board)
    print(structured)