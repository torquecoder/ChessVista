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

# Total chessboards to be grabbed from lichess.org
N = 20
image_no = 1

while image_no <= N:
    FEN = getRandomFEN()
    driver = webdriver.PhantomJS()
    driver.set_window_size(1024, 768)
    driver.get('https://lichess.org/analysis/standard/' + FEN)
    FEN = FEN.replace('/', '-')
    file_name = FEN + '.png'
    driver.save_screenshot('generated_images/' + file_name)
    im = Image.open('generated_images/' + file_name).crop([221,60,732,570]).save('generated_images/' + file_name)
    print ("Saved Image ", image_no)
    image_no += 1

driver.quit()


# Organize and crop already taken screenshots from chess.com
fen_array = ["k2B1rn1/1p2pp1P/P5PP/pqN2p1P/2P5/K2bpp1P/PrBb2pQ/1RRn1N2 w - - 0 1", "RQ3n2/p1N1NrpP/PP1q1p2/np1PrPB1/1bp2P2/2pp2P1/4RPbp/K4Bk1 w - - 0 1",
            "5Rnk/1P3Pqp/1K1Np3/pP1bN1r1/Pp1rP1P1/p1P3B1/1P1p1pQp/n1R3bB w - - 0 1", "BNb1rB1q/6pP/P2K4/1prn2Rp/Qp1P1p1P/Pp2bpPP/P1R1n1p1/1N2k3 w - - 0 1",
            "k7/prP1Rp2/4Pqbn/b5P1/BBKpNppP/ppP1PR1N/1p3PPr/2Q2n2 w - - 0 1", "8/PNnp1np1/ppPbPkPp/4NBp1/rpR1R1Q1/1P1PpqB1/PP1r4/2Kb4 w - - 0 1"]

for i in range (0, 6):
    FEN = fen_array[i].replace('/', '-')
    file_name = FEN + '.png'
    current_name = str(i + 1) + ".png"
    im = Image.open("chess.com_screenshots/" + current_name).crop([400,160,1280,1040]).save('generated_images/' + file_name)
    print ("Saved Image ", image_no)
    image_no += 1
