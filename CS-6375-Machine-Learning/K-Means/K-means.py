from skimage import io
from sklearn.cluster import KMeans
import numpy as np
import sys
import warnings
warnings.simplefilter("ignore", UserWarning)



k_value = int(sys.argv[1])
image_path = sys.argv[2]
 
image = io.imread(image_path)

rows = image.shape[0]
cols = image.shape[1]
  
image = image.reshape(image.shape[0]*image.shape[1],3)
kmeans = KMeans(n_clusters = k_value)

kmeans.fit(image)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8) 
labels = np.asarray(kmeans.labels_,dtype=np.uint8 )  
labels = labels.reshape(rows,cols); 

np.save('clusters.npy',clusters)    
centers = np.load('clusters.npy')

io.imsave('image.png',labels)
image1 = io.imread('image.png')


image2 = np.zeros((rows,cols,3),dtype=np.uint8 )
for i in range(rows):
    for j in range(cols):
            image2[i,j,:] = centers[image1[i,j],:]
io.imsave('quantized_image.jpg',image2);
