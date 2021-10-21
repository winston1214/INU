import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, h=1):
    # https://en.wikipedia.org/wiki/Gaussian_function
    return np.exp(-x**2 / (2 * h ** 2)) / (h * np.sqrt(2 * np.pi))


def draw_data(ax, x, hy=1.0, c='r'):
    # Draw data
    len_x = x.shape[0]
    for nidx_x in range(len_x):
        ax.plot([x[nidx_x], x[nidx_x]], [0, hy], ':', color=c)


if __name__ == "__main__":
    X = np.array([2.2])

    # Plot all available kernels
    X_plot = np.linspace(-1, 6, 100)[:, None]
    bins = np.linspace(0, 5, 21)
    bins[1]-bins[0]
    fig, ax = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(14,8))
    fig.subplots_adjust(left=0.05, right=0.95, hspace=0.05, wspace=0.05)

    bins = np.linspace(-1, 5, 16)
    bins[1]-bins[0]
    draw_data(ax[0, 0], X)
    ax[0, 0].hist(X[:], bins=bins, fc='#AAAAFF', density=False)
    ax[0, 0].text(0, 1.25, "Histogram, NOT NORMED, bin=0.4")

    bins = np.linspace(-1, 5, 9)
    bins[1]-bins[0]
    draw_data(ax[0, 1], X)
    ax[0, 1].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', density=True)
    ax[0, 1].text(0, 1.25, "Histogram, normed, bin=0.75")

    bins = np.linspace(-1, 5, 5)
    bins[1]-bins[0]
    draw_data(ax[0, 2], X)
    ax[0, 2].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', density=True)
    ax[0, 2].text(0, 1.25, "Histogram, normed, bin=1.5")

    draw_data(ax[1, 0], X)
    ax[1, 0].fill(X_plot, gaussian(X_plot-X[0]), '-k', fc='#AAAAFF')
    ax[1, 0].text(0, 1.25, "Gaussian, middle on X=2.2, h=1")

    draw_data(ax[1, 1], X)
    ax[1, 1].fill(X_plot, gaussian(X_plot-X[0], 0.6), '-k', fc='#AAAAFF')
    ax[1, 1].text(0, 1.25, "Gaussian, middle on X=2.2, h=0.6")

    draw_data(ax[1, 2], X)
    ax[1, 2].fill(X_plot, gaussian(X_plot-X[0], 0.35), '-k', fc='#AAAAFF')
    ax[1, 2].text(0, 1.25, "Gaussian, middle on X=2.2, h=0.35")

    plt.show()

    fig.savefig("kde_1data.jpg")
    print("SAVED")

