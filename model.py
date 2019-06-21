import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from tensorflow.keras.models import Model


def vgg16(im_dir):

	base_model = VGG16(weights='imagenet')
	model = Model(inputs=base_model.input, outputs=(base_model.get_layer('block5_pool').output, base_model.get_layer('block5_conv3').output, base_model.layers[-1].output))
	img = image.load_img(im_dir, target_size=(224, 224))

	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	# all_wg = base_model.layers[-1].get_weights()[0]
	pool, relu, pred = model.predict(x)
	pool_resized = tf.image.resize(pool, (14, 14))
	features = tf.concat([relu, pool_resized], axis=0)

	return features, pred