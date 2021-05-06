def init_row(row_num):
    board_tiles = [False] * NUM_TILES

    for i in range(NUM_TILES_PER_ROW):
        board_tiles[row_num * NUM_TILES_PER_ROW + i] = True

    return board_tiles


def init_column(column_num):
    board_tiles = [False] * NUM_TILES

    for i in range(NUM_TILES_PER_ROW):
        board_tiles[column_num + i * NUM_TILES_PER_ROW] = True

    return board_tiles


NUM_TILES = 64
NUM_TILES_PER_ROW = 8

FIRST_ROW = init_row(0)
SECOND_ROW = init_row(1)
THIRD_ROW = init_row(2)
FOURTH_ROW = init_row(3)
FIFTH_ROW = init_row(4)
SIXTH_ROW = init_row(5)
SEVENTH_ROW = init_row(6)
EIGHTH_ROW = init_row(7)

FIRST_COLUMN = init_column(0)
SECOND_COLUMN = init_column(1)
THIRD_COLUMN = init_column(2)
FOURTH_COLUMN = init_column(3)
FIFTH_COLUMN = init_column(4)
SIXTH_COLUMN = init_column(5)
SEVENTH_COLUMN = init_column(6)
EIGHTH_COLUMN = init_column(7)






