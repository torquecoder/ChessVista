from selenium import webdriver
import numpy as np
import os
from PIL import Image

def getRandomFEN():
    fen_chars = list('1KQRBNPkqrbnp')
    pieces = np.random.choice(fen_chars, 64)
    fen = '/'.join([''.join(pieces[i * 8 : (i + 1) * 8]) for i in range(8)])
    return fen

folder_name = "generated_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

pieceSets = ["cburnett", "merida", "alpha", "pirouetti", "chessnut", "chess7", "reillycraig", "companion", "fantasy", "spatial", "shapes", "letter"]

# Total chessboards to be grabbed
N = 1
image_no = 1

while image_no <= N:
    FEN = getRandomFEN()
    driver = webdriver.PhantomJS()
    driver.set_window_size(1024, 768)
    driver.get('https://lichess.org/analysis/standard/' + FEN)
    FEN = FEN.replace('/','-')
    file_name = FEN + '.png'
    driver.save_screenshot('generated_images/' + file_name)
    im = Image.open('generated_images/' + file_name).crop([221,60,732,570]).save('generated_images/' + file_name)
    print ("Saved Image ", image_no)
    image_no += 1

driver.quit()
