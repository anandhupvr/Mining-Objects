import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def find_item(feat):
	item = []
	item_values = []
	for i in range(14):
		for j in range(14):
			if feat[i, j] > 0:
				item.append([i, j])
				item_values.append(feat[i, j])

	return item, item_values


def bbox_plot(img, box, map):
	plt.imshow(map)
	plt.show()

	fig, ax = plt.subplots(1)
	# import pdb; pdb.set_trace()
	ax.imshow(img)
	for i in range(len(box)):
		k = 0
		s = patches.Rectangle((box[i][k], box[i][k+1]), box[i][k+2], box[i][k+3], linewidth=1, edgecolor='r', facecolor="none")
		ax.add_patch(s)
	plt.show()