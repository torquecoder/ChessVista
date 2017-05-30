# Imports
import tensorflow as tf
import numpy as np

# Whether or not suppress printing of small floating point values using scientific notation
np.set_printoptions(supress = True)

# Enter an interactive TensorFlow Session.
sess = tf.InteractiveSession()

# Import for visualization
import PIL.Image
from cStringIO import StringIO #This module implements a file-like class, StringIO, that reads and writes a string buffer

# Display an array as a picture
def display_array(a, format = 'jpeg', rng = [0, 1]):
    a = (a - rng[0]) / float(rng[1] - rng[0]) * 255
    a = np.uint8(np.clip(a, 0, 255))
    file = StringIO()
    PIL.Image.fromarray(a).save(file, format)
    display(Image(data = file.getValue()))

img_file = 
