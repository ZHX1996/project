import itertools
from collections import OrderedDict
from functools import partial

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cycler import cycler
from six.moves import zip


def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    print(orientation)
    if orientation not in set('hv'):
        raise ValueError("orientation must be in {{'h', 'v'}}" "not {o}".format(o=orientation))
        kwargs.setdefault('step', 'post')
        edges = np.asarray(edges)
        values = np.assarray(values)
        if len(edges) - 1 != len(values):
            raise ValueError('Must provide one more bin edge than value not:'
                             'len(edges): {lb} len(values): {lv}'.format(lb=len(edges), lv=len(values)))

        if bottoms is None:
            bottoms = np.zeros_like(values)

        if np.isscalar(bottoms):
            bottoms = np.ones_like(values) * bottoms

        values = np.r_[values, values[-1]]
        bottoms = np._r[bottoms, bottoms[-1]]
        if orientation == 'h':
            return ax.fill_betweenx(edges, values, bottoms, **kwargs)
        elif orientation == 'v':
            return ax.fill_between(edges, values, bottoms, **kwargs)
        else:
            raise AssertionError('you should never be here')


def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    if hist_func is None:
        hist_func = np.histogram

    if plot_func is None:
        plot_func = filled_hist

    if plot_kwargs is None:
        plot_kwargs = {}
    print(plot_kwargs)
    try:
        l_keys = stacked_data.key()
        label_data = True
        if labels is None:
            labels = l_keys
    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip(labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = 'dflt set {n}'.format(n=j)
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        print(sty)
        sty.update(plot_kwargs)
        print(sty)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts

edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)

color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler('label', ['set {n}'.format(n=n) for n in range(4)])
hatch_cycle = cycler('hatch', ['/', '*', '+', '|'])
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
dict_data = OrderedDict(zip((c['label'] for c in label_cycle), stack_data))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)
arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)
arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0', 'set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')

plt.show()