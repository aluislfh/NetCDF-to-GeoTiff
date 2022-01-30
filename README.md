# NetCDF-to-GeoTiff
Convert NetCDF data to Geotiff format using CDO and GDAL.

For this conversion, the CDO (Climate Data Operators - https://code.mpimet.mpg.de/projects/cdo) and GDAL (https://gdal.org/index.html) software's are used.
Initially, the metadata about the dates of each time step are obtained within the netcdf file through the following command line:

“cdo showdate era5-mswep-gpcc.nc > list_dates.txt”

This command returns a list of dates like the one shown below:

1981-01-01 1981-02-01 ... 2019-11-01 2019-12-01

Subsequently, the original netcdf file is divided into new files of the same format but breaking down each time step into a separate files, for this the following command is used:

“cdo -splitsel,1 era5-mswep-gpcc.nc split_data_”

Through a cycle in a Python or Bash script, the list of dates obtained previously can be used to build and rename the resulting names of the new netcdf files created by dividing the original netcdf file by time steps. This procedure will allow us to obtain files like the ones listed below:

rf_era5-mswep-gpcc_198101.nc
rf_era5-mswep-gpcc_198102.nc
...
rf_era5-mswep-gpcc_201912.nc

In each of these files the precipitation grid variable is named “rf”. By iterating with a script through each of these netcdf files, the GDAL program can be used to convert them to Geotiff format, which can be done using the following command line:

“gdal_translate netcdf:"rf_era5-mswep-gpcc_YYYYMM.nc":rf rf_era5-mswep-gpcc_YYYYMM.tiff”

When executing the GDAL command for each file of each time period, we will be obtaining the new resulting Geotiff files, which would be listed as follows:

rf_era5-mswep-gpcc_198101.tif
...
rf_era5-mswep-gpcc_201912.tif

The source code for this conversion process is available at https://github.com/aluislfh/NetCDF-to-GeoTiff/
