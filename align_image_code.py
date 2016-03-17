import numpy as np
import matplotlib.pyplot as plt

def get_points(imname):
    im = plt.imread('./%s.jpg' % imname)/255.
    shape = im.shape
    box = np.array([[0,0],[shape[1],0],[0,shape[0]],[shape[1],shape[0]]])

    plt.imshow(im)
    print("Select left, right of forehead.")
    fore1 = np.array(plt.ginput(2,timeout=-1))
    print("Select in, peak, out of L/R eyebrows.")
    brows1 = np.array(plt.ginput(6,timeout=-1))
    print("Select left, right, top, bottom of L/R eyes.")
    eyes1 = np.array(plt.ginput(8,timeout=-1))
    print("Select left, right, tip, bottom of nose.")
    nose1 = np.array(plt.ginput(4,timeout=-1))
    print("Select left, right, top, bottom of mouth.")
    mouth1 = np.array(plt.ginput(4,timeout=-1))
    print("Select left, right of chin.")
    chin1 = np.array(plt.ginput(2,timeout=-1))
    print("Select eyebrow, eye, nose, mouth of L/R face.")
    ears1 = np.array(plt.ginput(8,timeout=-1))
    plt.close()

    f = np.concatenate((fore1, brows1, eyes1, nose1, mouth1, chin1, ears1, box))
    np.save('./%s.npy' % imname, f[:,::-1])

if __name__ == "__main__":
    print "YOLO"
