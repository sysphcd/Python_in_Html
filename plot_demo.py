import matplotlib.pyplot as plt
import numpy as np


def plot_sin():

    x = np.arange(0, 4*np.pi, 0.1)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig