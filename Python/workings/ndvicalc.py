"""NDVI calculation using GDAL."""

from osgeo import gdal
from osgeo import gdal_array

import numpy as np

# open a GDAL dataset
dataset = gdal.Open(
    '../../example/LE70220491999322EDC01_stack.gtif', gdal.GA_ReadOnly)

# define first bands datatype
image_datatype = dataset.GetRasterBand(1).DataType
print(image_datatype)

image = np.zeros((dataset.RasterYSize, dataset.RasterXSize, dataset.RasterCount),
                 dtype=gdal_array.GDALTypeCodeToNumericTypeCode(image_datatype))


# Loop over all bands in dataset
for b in range(dataset.RasterCount):
    # Remember, GDAL index is on 1,
    # but Python is on 0 -- so we add 1 for our GDAL calls
    band = dataset.GetRasterBand(b + 1)

    # Read in the band's data into the third dimension of our array
    image[:, :, b] = band.ReadAsArray()

print('Red band mean: {r}'.format(r=image[:, :, 2].mean()))
print('NIR band mean: {nir}'.format(nir=image[:, :, 3].mean()))

b_red = 2
b_nir = 3

ndvi = (image[:, :, b_nir] - image[:, :, b_red]) / \
    (image[:, :, b_red] + image[:, :, b_nir])

print(ndvi)
print(ndvi.max())
