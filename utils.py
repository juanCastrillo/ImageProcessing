import matplotlib.pyplot as plt
import numpy as np

def histogram(img, channels=1):
    '''
    Histogram
    '''
    H, W, C = img.shape
    channel_hist = img.reshape([H*W, C]) # R, G, B

    with plt.style.context("seaborn-v0_8-white"):
        if channels == 3:
            r_hist = channel_hist[:, 0]
            g_hist = channel_hist[:, 1]
            b_hist = channel_hist[:, 2]
            # plt.hist(r_hist, bins=256, color="r")
            # plt.hist(g_hist, bins=256, color="g")
            # plt.hist(b_hist, bins=256, color="b")
            plt.plot(np.log(np.histogram(r_hist, bins=256)[0]), color="r")
            plt.plot(np.log(np.histogram(g_hist, bins=256)[0]), color="g")
            plt.plot(np.log(np.histogram(b_hist, bins=256)[0]), color="b")
        else:
            hist = channel_hist.mean(axis=1)
            counts, bins = np.histogram(hist, bins=256)
            max_y = np.percentile(counts, 99)
            # plt.plot(np.clip(counts, 0, max_y) )
            plt.plot(np.log(counts) )
        plt.show()