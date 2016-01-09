import sys
import numpy as np

from matplotlib import pyplot as plt
from align_image_code import get_points
from scipy.spatial import Delaunay
from skimage.draw import polygon

def computeAffine(tri1_pts, tri2_pts):
    tri1 = np.ones([3,3])
    tri2 = np.ones([3,3])
    tri1[:,:-1] = tri1_pts
    tri2[:,:-1] = tri2_pts
    return np.dot(tri2.T, np.linalg.inv(tri1.T))

def morph(im1, im2, im1_pts, im2_pts, tri, warp_frac, dissolve_frac):
    result = np.empty(im1.shape)
    for triangle in tri.simplices:
        pts1 = im1_pts[triangle]
        pts2 = im2_pts[triangle]
        pts3 = warp_frac*pts1 + (1-warp_frac)*pts2
        A = computeAffine(pts3, pts1)
        B = computeAffine(pts3, pts2)
        rr, cc = polygon(pts3[:,0], pts3[:,1])
        vector = np.ones([3, len(rr)])
        vector[0] = rr
        vector[1] = cc
        A = np.dot(A, vector).astype(int)
        B = np.dot(B, vector).astype(int)
        result[rr, cc] = dissolve_frac*im1[A[0], A[1]] +\
                (1-dissolve_frac)*im2[B[0], B[1]]
    return result

def main(name1, name2):
    im1 = plt.imread('./%s.jpg' % name1)/255.
    im2 = plt.imread('./%s.jpg' % name2)/255.

    #get_points(name1)
    #get_points(name2)

    face1 = np.load('./%s.npy' % name1)
    face2 = np.load('./%s.npy' % name2)
    tri = Delaunay((face1+face2)/2)

    ## Morph Sequence
    for step in range(45):
        plt.imsave(('./%s%02d.jpg' % ((name1[:2]+name2[:2]),step)), \
                morph(im1, im2, face1, face2, tri, step/44., step/44.))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
