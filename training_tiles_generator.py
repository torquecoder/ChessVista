import chess_board_recognizer
import os

for image_name in os.listdir("ChessboardScreenshots"):
    chess_board_recognizer.generateTileset(image_name)
