import numpy as np
from numpy.testing import assert_equal, assert_array_equal
from nose.tools import assert_greater
from skimage.segmentation import felzenszwalb_segmentation


def test_grey():
    # very weak tests. This algorithm is pretty unstable.
    img = np.zeros((20, 20))
    img[:10, 10:] = 0.2
    img[10:, :10] = 0.4
    img[10:, 10:] = 0.6
    seg = felzenszwalb_segmentation(img, sigma=0)
    # we expect 4 segments:
    assert_equal(len(np.unique(seg)), 4)
    # that mostly respect the 4 regions:
    for i in xrange(4):
        hist = np.histogram(img[seg == i], bins=[0, 0.1, 0.3, 0.5, 1])[0]
        assert_greater(hist[i], 40)


def test_color():
    # very weak tests. This algorithm is pretty unstable.
    img = np.zeros((20, 20, 3))
    img[:10, :10, 0] = 1
    img[10:, :10, 1] = 1
    img[10:, 10:, 2] = 1
    seg = felzenszwalb_segmentation(img, sigma=0)
    # we expect 4 segments:
    assert_equal(len(np.unique(seg)), 4)
    assert_array_equal(seg[:10, :10], 0)
    assert_array_equal(seg[10:, :10], 2)
    assert_array_equal(seg[:10, 10:], 1)
    assert_array_equal(seg[10:, 10:], 3)


if __name__ == '__main__':
    from numpy import testing
    testing.run_module_suite()
