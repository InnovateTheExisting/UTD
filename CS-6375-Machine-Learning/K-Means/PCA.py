from skimage import io
import numpy as np
from sklearn.decomposition import PCA
import sys
from sklearn.preprocessing import MinMaxScaler
import scipy.misc
from scipy.misc import imsave

principle_components = int(sys.argv[1])
image_path = sys.argv[2]

image = io.imread(image_path)
image=image[:,:,:3] 

rows = image.shape[0]
cols = image.shape[1]
  
image = image.reshape(image.shape[0],image.shape[1]*3)
pca = PCA(n_components=principle_components, svd_solver='full')
pca.fit(image)
img = pca.transform(image)

xd = pca.inverse_transform(img)
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(xd)
xd=scaler.transform(xd)
xd = np.reshape(xd,(rows,cols,3))
rgb_image = scipy.misc.toimage(xd)

imsave('compressed_image.jpg',rgb_image)

