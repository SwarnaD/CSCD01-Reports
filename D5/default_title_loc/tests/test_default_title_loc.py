from __future__ import absolute_import, division, print_function

import six
from itertools import chain, product
from distutils.version import LooseVersion
import io

import datetime

import pytz

import numpy as np
from numpy import ma
from cycler import cycler
import pytest

import warnings

import matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import matplotlib.markers as mmarkers
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from numpy.testing import assert_allclose, assert_array_equal
from matplotlib.cbook import (
    IgnoredKeywordWarning, MatplotlibDeprecationWarning)


@image_comparison(baseline_images=['title_default_location_center'], extensions=['png'])
def test_title_default_location_center():
    test_default_title_loc = "center"
    matplotlib.rcParams['axes.titleloc'] = test_default_title_loc
    plt.plot(range(10))
    plt.title('Title')
    plt.show()


@image_comparison(baseline_images=['title_default_location_left'], extensions=['png'])
def test_title_default_location_left():
    test_default_title_loc = "left"
    matplotlib.rcParams['axes.titleloc'] = test_default_title_loc
    plt.plot(range(10))
    plt.title('Title')
    plt.show()


@image_comparison(baseline_images=['title_default_location_right'], extensions=['png'])
def test_title_default_location_right():
    test_default_title_loc = "right"
    matplotlib.rcParams['axes.titleloc'] = test_default_title_loc
    plt.plot(range(10))
    plt.title('Title')
    plt.show()