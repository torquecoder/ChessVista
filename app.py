import os
import glob
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
import chess_board_recognizer
import uuid
import tester


if not os.path.exists('user_chessboards'):
    os.makedirs('user_chessboards')
if not os.path.exists('user_tiles'):
    os.makedirs('user_tiles')


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'user_chessboards'
TILES_OUTPUT_FOLDER = 'user_tiles'
INDEX = 'index.html'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TILES_OUTPUT_FOLDER'] = TILES_OUTPUT_FOLDER
app.config['INDEX'] = INDEX

symbol = {'black_bishop': 'b', 'black_king': 'k', 'black_knight': 'n', 'black_pawn': 'p', 'black_queen': 'q', 'black_rook': 'r', 'blank': 'e', \
'white_bishop': 'B', 'white_king': 'K', 'white_knight': 'N', 'white_pawn': 'P', 'white_queen': 'Q', 'white_rook': 'R'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def createFEN(test_result):
    FEN = ''
    rows = 8
    while rows > 0:
        rows -= 1
        st = rows
        en = 63 - (7 - rows)
        blanks = 0
        for idx in range(st, en + 1, 8):
            if (test_result[idx] == 'blank'):
                blanks += 1
            else:
                if (blanks > 0):
                    FEN += str(blanks)
                    blanks = 0
                FEN += symbol[test_result[idx]]
        if (blanks > 0):
            FEN += str(blanks)
            blanks = 0
        if rows != 0:
            FEN += '/'
    #print(FEN)
    return FEN

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No image part')
            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No image selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            random_file_name = str(uuid.uuid4())
            file.filename = random_file_name + '.' + file.filename.rsplit('.', 1)[1].lower() # Some unique file name
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            chess_board_recognizer.generateTileset(file.filename, app.config['UPLOAD_FOLDER'], app.config['TILES_OUTPUT_FOLDER'])
            tiles_array = []
            tiles_location = TILES_OUTPUT_FOLDER + '/squares_' + random_file_name
            path = os.path.join(tiles_location, '*g')  # For finding all .jpeg, .jpg, .png files
            tiles = sorted(glob.glob(path))
            for tile in tiles:
                tiles_array.append(tile)
            test_result = tester.testTiles(tiles_array)
            FEN = createFEN(test_result)
            return render_template('analysis.html', fen = FEN)
            #return redirect(url_for('uploaded_file', filename=filename))

    return render_template('index.html')

if __name__ == '__main__':
   app.run()
