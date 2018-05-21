import numpy as np
from numpy import linalg
from numpy.linalg import norm
from scipy.spatial.distance import squareform, pdist

import sklearn
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

from sklearn.metrics.pairwise import pairwise_distances
from sklearn.manifold.t_sne import (_joint_probabilities,
                                    _kl_divergence)
# from sklearn.utils.extmath import _ravel

RS = 20150101

import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import matplotlib

import seaborn as sns
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1.5, rc={"lines.linewidth":2.5})

from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy


digits = load_digits()
print(digits.data.shape)
# print(digits['DESCR'])


def dataset():
    nrows, ncols = 2, 5
    plt.figure(figsize=(6,3))
    plt.gray()
    for i in range(ncols * nrows):
        ax = plt.subplot(nrows, ncols, i+1)
        ax.matshow(digits.images[i,...])
        plt.xticks([]); plt.yticks([])
        plt.title(digits.target[i])
    # plt.show()

X = np.vstack([digits.data[digits.target == i]
                   for i in range(10)])
y = np.hstack([digits.target[digits.target == i]
                   for i in range(10)])


def scatter(x, colors):
    # choose a color palette with seaborn
    palette = np.array(sns.color_palette('hls', 10))

    # create a scatter plot
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:, 0], x[:, 1], lw=0, s=40, c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

    # add a labels for each digit
    txts = []
    for i in range(10):
        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([PathEffects.Stroke(linewidth=5, foreground='w'),
                              PathEffects.Normal()])
        txts.append(txt)
    return f, ax, sc, txts


# reorder the data points according to the handwritten numbers
def tsne():
    digits_proj = TSNE(random_state=RS).fit_transform(X)
    # print(digits_proj.shape)
    scatter(digits_proj, y)
    plt.show()
    # f, ax, sc, txts = scatter(digits_proj, y)
    #
    # def make_frame_mpl(t):
    #     i = int(t*40)
    #     x = digits_proj[..., i]
    #     sc.set_offsets(x)
    #     for j, txt in zip(range(10), txts):
    #         xtext, ytext = np.median(x[y == j, :], axis=0)
    #         txt.set_x(xtext)
    #         txt.set_y(ytext)
    #     return mplfig_to_npimage(f)
    #
    # animation = mpy.VideoClip(make_frame_mpl, duration=digits_proj.shape[1]/40.)
    # animation.write_gif("D://animation.gif", fps=20)


def similarity_matrix():
    def _joint_probabilities_constant_sigma(D, sigma):
        P = np.exp(-D**2/2 * sigma**2)
        P /= np.sum(P, axis=1)
        return P

    # Pairwise_distances between all data points
    D = pairwise_distances(X, squared=True)
    # Similarity with constant sigma
    P_constant = _joint_probabilities_constant_sigma(D, .002)
    # Similarity with variable sigma
    P_binary = _joint_probabilities(D, 30., False)
    # The output of this function needs to be reshaped to a square matrix
    P_binary_s = squareform(P_binary)

    plt.figure(figsize=(12, 4))
    pal = sns.light_palette("blue", as_cmap=True)

    plt.subplot(131)
    plt.imshow(D[::10, ::10], interpolation='none', cmap=pal)
    plt.axis('off')
    plt.title('Distance matrix', fontdict={'fontsize':16})

    plt.subplot(132)
    plt.imshow(P_constant[::10, ::10], interpolation='none', cmap=pal)
    plt.axis('off')
    plt.title("$p_{j|i}$ (constant $\sigma$)", fontdict={'fontsize':16})

    plt.subplot(133)
    plt.imshow(P_binary_s[::10, ::10], interpolation='none', cmap=pal)
    plt.axis('off')
    plt.title("$p_{j|i}$ (variable $\sigma$)", fontdict={'fontsize':16})
    # plt.show()


def physical_analogy():
    positions = []

    def _gradient_descent(objective, p0, it, n_iter, n_iter_check=1, n_iter_without_progress=30,
                          momentum=0.5, learning_rate=1000.0,
                          min_gain=0.01, min_grad_norm=1e-7,
                          min_error_diff=1e-7, verbose=0,
                          args=None, kwargs=None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        p = p0.copy().ravel()
        update = np.zeros_like(p)
        gains = np.ones_like(p)
        error = np.finfo(np.float).max  # finfo机器精度
        best_error = np.finfo(np.float).max
        best_iter = 0

        for i in range(it, n_iter):
            positions.append(p.copy())

            new_error, grad = objective(p, *args)
            error_diff = np.abs(new_error - error)
            error = new_error
            grad_norm = linalg.norm(grad)

            if error < best_error:
                best_error = error
                best_iter = i
            elif i - best_iter > n_iter_without_progress:
                break
            if min_grad_norm >= grad_norm:
                break
            if min_error_diff >= error_diff:
                break

            inc = update * grad >= 0.0
            dec = np.invert(inc)
            gains[inc] += 0.05
            gains[dec] *= 0.95
            np.clip(gains, min_gain, np.inf)
            grad *= gains
            update = momentum * update - learning_rate * grad
            p += update

        return p, error, i
    sklearn.manifold.t_sne._gradient_descent = _gradient_descent

    X_proj = TSNE(random_state=RS).fit_transform(X)
    X_iter = np.dstack(position.reshape(-1, 2)
                       for position in positions)

    f, ax, sc, txts = scatter(X_iter[..., -1], y)

    def make_frame_mpl(t):
        i = int(t*40)
        x = X_iter[..., i]
        sc.set_offsets(x)
        for j, txt in zip(range(10), txts):
            xtext, ytext = np.median(x[y == j, :], axis=0)
            txt.set_x(xtext)
            txt.set_y(ytext)
        return mplfig_to_npimage(f)

    animation = mpy.VideoClip(make_frame_mpl, duration=X_iter.shape[2]/40.)
    animation.write_gif("D://animation.gif", fps=20)

if __name__ == '__main__':
    physical_analogy()
    # tsne()