import os
import glob
from PIL import Image

def organize(output_directory, input_directory):

    if not os.path.exists(output_directory + "/white_pawn"):
        os.makedirs(output_directory + "/white_pawn")

    if not os.path.exists(output_directory + "/black_pawn"):
        os.makedirs(output_directory + "/black_pawn")

    if not os.path.exists(output_directory + "/white_knight"):
        os.makedirs(output_directory + "/white_knight")

    if not os.path.exists(output_directory + "/black_knight"):
        os.makedirs(output_directory + "/black_knight")

    if not os.path.exists(output_directory + "/white_bishop"):
        os.makedirs(output_directory + "/white_bishop")

    if not os.path.exists(output_directory + "/black_bishop"):
        os.makedirs(output_directory + "/black_bishop")

    if not os.path.exists(output_directory + "/white_rook"):
        os.makedirs(output_directory + "/white_rook")

    if not os.path.exists(output_directory + "/black_rook"):
        os.makedirs(output_directory + "/black_rook")

    if not os.path.exists(output_directory + "/white_queen"):
        os.makedirs(output_directory + "/white_queen")

    if not os.path.exists(output_directory + "/black_queen"):
        os.makedirs(output_directory + "/black_queen")

    if not os.path.exists(output_directory + "/white_king"):
        os.makedirs(output_directory + "/white_king")

    if not os.path.exists(output_directory + "/black_king"):
        os.makedirs(output_directory + "/black_king")

    if not os.path.exists(output_directory + "/blank"):
        os.makedirs(output_directory + "/blank")

    white_pawn_idx = 1
    black_pawn_idx = 1
    white_knight_idx = 1
    black_knight_idx = 1
    white_bishop_idx = 1
    black_bishop_idx = 1
    white_rook_idx = 1
    black_rook_idx = 1
    white_queen_idx = 1
    black_queen_idx = 1
    white_king_idx = 1
    black_king_idx = 1
    blank_idx = 1

    for fld in os.listdir(input_directory):
        path = os.path.join(input_directory, fld, '*g')  # For finding all .jpeg, .jpg, .png files
        files = glob.glob(path)
        for fl in files:
            if ("A1" in fl) or ("B1" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_pawn/" + "white_pawn" + str(white_pawn_idx) + ".png"
                img.save(location)
                white_pawn_idx += 1
            elif ("C1" in fl) or ("D1" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_pawn/" + "black_pawn" + str(black_pawn_idx) + ".png"
                img.save(location)
                black_pawn_idx += 1
            elif ("E1" in fl) or ("F1" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_knight/" + "white_knight" + str(white_knight_idx) + ".png"
                img.save(location)
                white_knight_idx += 1
            elif ("G1" in fl) or ("H1" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_knight/" + "black_knight" + str(black_knight_idx) + ".png"
                img.save(location)
                black_knight_idx += 1
            elif ("A2" in fl) or ("B2" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_bishop/" + "white_bishop" + str(white_bishop_idx) + ".png"
                img.save(location)
                white_bishop_idx += 1
            elif ("C2" in fl) or ("D2" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_bishop/" + "black_bishop" + str(black_bishop_idx) + ".png"
                img.save(location)
                black_bishop_idx += 1
            elif ("E2" in fl) or ("F2" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_rook/" + "white_rook" + str(white_rook_idx) + ".png"
                img.save(location)
                white_rook_idx += 1
            elif ("G2" in fl) or ("H2" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_rook/" + "black_rook" + str(black_rook_idx) + ".png"
                img.save(location)
                black_rook_idx += 1
            elif ("A3" in fl) or ("B3" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_queen/" + "white_queen" + str(white_queen_idx) + ".png"
                img.save(location)
                white_queen_idx += 1
            elif ("C3" in fl) or ("D3" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_queen/" + "black_queen" + str(black_queen_idx) + ".png"
                img.save(location)
                black_queen_idx += 1
            elif ("E3" in fl) or ("F3" in fl):
                img = Image.open(fl)
                location = output_directory + "/white_king/" + "white_king" + str(white_king_idx) + ".png"
                img.save(location)
                white_king_idx += 1
            elif ("G3" in fl) or ("H3" in fl):
                img = Image.open(fl)
                location = output_directory + "/black_king/" + "black_king" + str(black_king_idx) + ".png"
                img.save(location)
                black_king_idx += 1
            else:
                img = Image.open(fl)
                location = output_directory + "/blank/" + "blank" + str(blank_idx) + ".png"
                img.save(location)
                blank_idx += 1
