import os, sys, glob
import numpy as np

# data directory
os.chdir('/media/adrian/HDD_pc/adrian/GIS')

# nc imput
ncfile = 'era5-mswep-gpcc.nc'

# CDO Split
os.system('cdo showdate '+ncfile+' > list.txt')
os.system('cdo -splitsel,1 '+ncfile+' split_')

# Saving and listing dates of ncfile
flist = open('list.txt', 'r')
fline = flist.readline()
fline_fix = fline[2:].split('  ')

fglob = sorted(glob.glob('split_*.nc'))

for fl,fg in zip(fline_fix,fglob):

    fdate = fl.split('-')[0]+fl.split('-')[1]    # 1981-02-01

    # rename nc files
    os.system('mv '+fg+' rf_'+ncfile.split('.')[0]+'_'+fdate+'.nc')  # era5-mswep-gpcc

    # convert to geotiff

    print('gdal_translate NETCDF:\"rf_'+ncfile.split('.')[0]+'_'+fdate+'.nc\":rf rf_'+ncfile.split('.')[0]+'_'+fdate+'.tif')
    os.system('gdal_translate NETCDF:\"rf_'+ncfile.split('.')[0]+'_'+fdate+'.nc\":rf rf_'+ncfile.split('.')[0]+'_'+fdate+'.tif') 

