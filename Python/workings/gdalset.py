"""Plaground for GDAL class."""
from osgeo import gdal

# print ("GDAL's version is", gdal.__version__)
# print (gdal)
dataset = gdal.Open(
    '../../example/LE70220491999322EDC01_stack.gtif', gdal.GA_ReadOnly)
# print (dataset)

num_bands = dataset.RasterCount
metadata = dataset.GetMetadata()
description = dataset.GetDescription()
# print (num_bands, metadata, description)
band1 = dataset.GetRasterBand(1)
print(band1.DataType)

datatype_name = gdal.GetDataTypeName(band1.DataType)
print('Band datatype: {dt}'.format(dt=datatype_name))
print(band1.ReadAsArray)
