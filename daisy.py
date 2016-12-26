from skimage.feature import daisy
from skimage import data
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image


# img = data.camera()
# img = Image.open("worker.tif")
img = io.imread('worker.tif', as_grey = True)
descs, descs_img = daisy(img, step=180, radius=58, rings=2, histograms=6, orientations=8, visualize=True)

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(descs_img)
descs_num = descs.shape[0] * descs.shape[1]
ax.set_title('%i DAISY descriptors extracted:' % descs_num)
plt.show()
