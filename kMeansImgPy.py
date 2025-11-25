# I've left some code in comments so that it can be easier if one wants to test and see output at various points. To make things simpler just remove the commented code !

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import utils
import cv2
import numpy as np
import pandas as pd

def kMeansImage(img):
    image = img
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    nC = 3              # No. of Clusters

    # reshape the image to a list of pixels
    image = image.reshape((image.shape[0]*image.shape[1],3))

    # cluster the pixel intensities
    clt = KMeans(n_clusters=nC)
    clt.fit(image)

    # build a histogram of clusters 
    hist = utils.centroid_histogram(clt)
    
    # ERROR FIX: We focus on the labels, we don't need to print the list to console to make it work
    colors = clt.cluster_centers_
    labelsIndex = pd.Series(clt.labels_).value_counts().to_frame()
    
    # Logic to find the most dominant color
    maxIndex = labelsIndex.index.values     
    maxColorIndex = maxIndex[0]             
    
    # Numpy array to list of colors
    colorsList = colors[maxColorIndex].tolist()

    # IMPORTANT for Web: Comment out plot/show commands so they don't crash the server
    # bar = utils.plot_colors(hist, clt.cluster_centers_)
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(bar)
    # plt.show()

    return colorsList