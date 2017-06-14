import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import os
import glob
import numpy as np
import cv2


def testTiles(tile_paths):


    classes = ['black_bishop', 'black_king', 'black_knight', 'black_pawn', 'black_queen', 'black_rook', 'blank', \
    'white_bishop', 'white_king', 'white_knight', 'white_pawn', 'white_queen', 'white_rook']

    session = tf.Session()
    saver = tf.train.import_meta_graph('trained_model/trained_model-15000.meta')
    saver.restore(session, tf.train.latest_checkpoint('trained_model/'))
    graph = tf.get_default_graph()



    y_pred = graph.get_tensor_by_name("y_pred:0")

    for image_path in tile_paths:

        # First, load the image
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #image_path="/test_data/blank/blank12.png"
        filename = image_path
        image_size = 32
        images = []
        image = cv2.imread(filename)

        images.append(image)
        images = np.array(images, dtype = np.uint8)
        images = images.astype('float32')
        images = images / 255

        x= graph.get_tensor_by_name("x:0")
        img_size = 32
        num_channels = 3
        img_size_flat = img_size * img_size * num_channels
        x_batch = images.reshape(1, img_size_flat)
        y_true = graph.get_tensor_by_name("y_true:0")
        y_test_images = np.zeros((1, 13)) # 13 => number of classes
        feed_dict_testing = {x: x_batch, y_true: y_test_images}
        result = session.run(y_pred, feed_dict = feed_dict_testing)
        #print(result)
        index = np.argmax(result)
        print(classes[index])
