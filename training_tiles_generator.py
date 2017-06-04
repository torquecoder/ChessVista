import chess_board_recognizer
import os

for image_name in os.listdir("training_chessboards"):
    chess_board_recognizer.generateTileset(image_name)
