import os
import glob
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import chess_board_recognizer
import uuid


if not os.path.exists('uploads'):
    os.makedirs('uploads')
if not os.path.exists('user_tiles'):
    os.makedirs('user_tiles')
    
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
TILES_OUTPUT_FOLDER = 'user_tiles'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TILES_OUTPUT_FOLDER'] = TILES_OUTPUT_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            file.filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower() # Some unique file name
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            chess_board_recognizer.generateTileset(file.filename, app.config['UPLOAD_FOLDER'], app.config['TILES_OUTPUT_FOLDER'])
            #return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload Chessboard Image</title>
    <h1>Upload Chessboard Image</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''