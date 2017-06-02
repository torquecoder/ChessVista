import chess_board_recognizer
import os

input_chessboard_folder = "training_chessboards"
output_tile_folder = "training_tiles"

if not os.path.exists(output_tile_folder):
    os.makedirs(output_tile_folder)

chess_board_recognizer.generateTileset(input_chessboard_folder, output_tile_folder)
