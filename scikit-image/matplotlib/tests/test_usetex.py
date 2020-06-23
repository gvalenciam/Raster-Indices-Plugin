import numpy as np
import pytest
import platform

import matplotlib as mpl
from matplotlib.testing.decorators import check_figures_equal, image_comparison
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


if not mpl.checkdep_usetex(True):
    pytestmark = pytest.mark.skip('Missing TeX of Ghostscript or dvipng')


@image_comparison(
    baseline_images=['test_usetex'],
    extensions=['pdf', 'png'],
    style="mpl20")
def test_usetex():
    mpl.rcParams['text.usetex'] = True
    fig = plt.figure()
    ax = fig.add_subplot(111)
    kwargs = {"verticalalignment": "baseline", "size": 24,
              "bbox": dict(pad=0, edgecolor="k", facecolor="none")}
    ax.text(0.2, 0.7,
            # the \LaTeX macro exercises character sizing and placement,
            # \left[ ... \right\} draw some variable-height characters,
            # \sqrt and \frac draw horizontal rules, \mathrm changes the font
            r'\LaTeX\ $\left[\int\limits_e^{2e}'
            r'\sqrt\frac{\log^3 x}{x}\,\mathrm{d}x \right\}$',
            **kwargs)
    ax.text(0.2, 0.3, "lg", **kwargs)
    ax.text(0.4, 0.3, r"$\frac{1}{2}\pi$", **kwargs)
    ax.text(0.6, 0.3, "$p^{3^A}$", **kwargs)
    ax.text(0.8, 0.3, "$p_{3_2}$", **kwargs)
    for x in {t.get_position()[0] for t in ax.texts}:
        ax.axvline(x)
    for y in {t.get_position()[1] for t in ax.texts}:
        ax.axhline(y)
    ax.set_axis_off()


@check_figures_equal()
def test_empty(fig_test, fig_ref):
    mpl.rcParams['text.usetex'] = True
    fig_test.text(.5, .5, "% a comment")


@check_figures_equal()
def test_unicode_minus(fig_test, fig_ref):
    mpl.rcParams['text.usetex'] = True
    fig_test.text(.5, .5, "$-$")
    fig_ref.text(.5, .5, "\N{MINUS SIGN}")


def test_mathdefault():
    plt.rcParams["axes.formatter.use_mathtext"] = True
    fig = plt.figure()
    fig.add_subplot().set_xlim(-1, 1)
    # Check that \mathdefault commands generated by tickers don't cause
    # problems when later switching usetex on.
    mpl.rcParams['text.usetex'] = True
    fig.canvas.draw()
