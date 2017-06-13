import chess_board_recognizer
import os
import dataset_organizer

# Generating tiles for training
for image_name in os.listdir("training_chessboards"):
    chess_board_recognizer.generateTileset(image_name, "training_chessboards", "training_tiles")
dataset_organizer.organize("train_data", "training_tiles")

# Generating tiles for testing
for image_name in os.listdir("testing_chessboards"):
    chess_board_recognizer.generateTileset(image_name, "testing_chessboards", "testing_tiles")
dataset_organizer.organize("test_data", "testing_tiles")
