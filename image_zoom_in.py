import numpy as np
from tifffile import imread as tiff_imread
from tifffile import imsave as tiff_imsave
from scipy.ndimage import zoom as sci_zoom


def zoom_in(img, factor=1):
    zoomed = sci_zoom(img, factor)
    top_left = (int(zoomed.shape[0] / 2 - img.shape[0] / 2), int(zoomed.shape[1] / 2 - img.shape[1] / 2))
    bottom_right = (int(zoomed.shape[0] / 2 + img.shape[0] / 2), int(zoomed.shape[1] / 2 + img.shape[1] / 2))
    a = zoomed[top_left[0]:bottom_right[0], top_left[1]:bottom_right[1]]
    return a

def main():
    input = tiff_imread('lenna.tif')
    zoomed = zoom_in(input, 2.2)
    tiff_imsave('zoomed_22.tif', zoomed)
    tiff_imsave('zoomed_33.tif', zoom_in(input, 3.3))
    tiff_imsave('zoomed_5.tif', zoom_in(input, 5))


if __name__ == "__main__":
    main()
