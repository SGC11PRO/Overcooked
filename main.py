# We can enlarge pyxel color palette by defining a file with the extension .pyxpal and adding there the hex codes of the
# colors of the palette. More info at: https://github.com/kitao/pyxel/blob/main/docs/pyxres-format.md

from board import Board

# Constants
board_width = 192
board_height = 176

board_size = (board_width, board_height)

# initialize pyxel window by creating board obj
board = Board(board_size)