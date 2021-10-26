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
    X = np.random.normal(2.5, 0.9, 14)
    N = len(X)

    # Plot all available kernels
    X_plot = np.linspace(-1, 7, 100)[:, None]
    bins = np.linspace(-1, 5, 20)
    bins[1] - bins[0]
    fig, ax = plt.subplots(2, 3, sharex=True, figsize=(14, 8))
    fig.subplots_adjust(left=0.05, right=0.95, hspace=0.05, wspace=0.05)
    ax[0, 0].set_ylim([0, 3.1])
    ax[0, 1].set_ylim([0, 1])
    ax[0, 2].set_ylim([0, 1])
    ax[1, 0].set_ylim([0, 1])
    ax[1, 1].set_ylim([0, 1])
    ax[1, 2].set_ylim([0, 1])

    draw_data(ax[0, 0], X)
    ax[0, 0].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', density=False)
    ax[0, 0].text(0, 2.8, "Histogram, bin=0.32")

    bins = np.linspace(-1, 5, 9)
    bins[1] - bins[0]
    draw_data(ax[0, 1], X)
    ax[0, 1].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', density=True)
    ax[0, 1].text(0, 0.9, "Histogram, normed, bin=0.75")

    bins = np.linspace(-1, 5, 5)
    bins[1] - bins[0]
    draw_data(ax[0, 2], X)
    ax[0, 2].hist(X[:], bins=bins + 0.75, fc='#AAAAFF', density=True)
    ax[0, 2].text(0, 0.9, "Histogram, normed, bin=1.5")

    sum1 = np.zeros(len(X_plot))
    sum2 = np.zeros(len(X_plot))
    sum3 = np.zeros(len(X_plot))
    draw_data(ax[1, 0], X)
    draw_data(ax[1, 1], X)
    draw_data(ax[1, 2], X)

    for i in range(0, N):
        sum1 = sum1 + gaussian(X_plot - X[i]) # 201600779 김영민
        sum2 = sum2 +  gaussian(X_plot-X[i],0.6) # 201600779 김영민
        sum3 = sum3 + gaussian(X_plot-X[i],0.35) # 201600779 김영민
        pass
    sum1 = sum1/N # 201600779 김영민
    sum2 = sum2/N # 201600779 김영민
    sum3 = sum3/N # 201600779 김영민

    ax[1, 0].fill(X_plot, sum1, '-k', fc='#AAAAFF')
    ax[1, 0].text(0, 0.9, "Gaussian, h=1")
    ax[1, 1].fill(X_plot, sum2, '-k', fc='#AAAAFF')
    ax[1, 1].text(0, 0.9, "Gaussian, h=0.6")
    ax[1, 2].fill(X_plot, sum3, '-k', fc='#AAAAFF')
    ax[1, 2].text(0, 0.9, "Gaussian, h=0.35")

    plt.show()

    fig.savefig("kde_mdata_tmp.jpg")
    print("SAVED")
