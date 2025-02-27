To build a simple deb installation file, follow the general instructions at:
  https://ubuntuforums.org/showthread.php?t=910717

Example will be with volcano-ash3d-projection
1) Prepare the source
     This repo does not have an official release, just provisional. We get the 'master' branch
     and call it v1.0
  wget https://code.usgs.gov/vsc/ash3d/volcano-ash3d-projection/-/archive/master/volcano-ash3d-projection-master.zip
  unzip volcano-ash3d-projection-master.zip

2) Create the directory structure
  mkdir -p BUILD
  mkdir -p BUILD/volcano-ash3d-projection-1.0-1/DEBIAN
  mkdir -p BUILD/volcano-ash3d-projection-1.0-1/opt/USGS/lib
  mkdir -p BUILD/volcano-ash3d-projection-1.0-1/opt/USGS/include
  mkdir -p BUILD/volcano-ash3d-projection-1.0-1/opt/USGS/bin

3) Make the control file.
 vi BUILD/volcano-ash3d-projection-1.0-1/DEBIAN/control
Package: volcano-ash3d-projection
Version: 1.0
Architecture: i386
Maintainer: Hans Schwaiger <hschwaiger@usgs.gov>
Depends: 
Installed-Size:
Homepage: https://code.usgs.gov/vsc/ash3d/volcano-ash3d-projection
Description: libprojection is a fortran 90 module that contains subroutines that can convert between lon,lat and various projections commonly used in numerical
 weather prediction forecast/reanalysis products.

4) Now consider the directory BUILD/volcano-ash3d-projection-1.0-1/ as a system root and install
 cd volcano-ash3d-projection-master
 vi makefile (change INSTALLDIR to CWD/../BUILD/volcano-ash3d-projection-1.0-1/)
 make; make install

5) Finally, run the packager from BUILD
 dpkg-deb --build volcano-ash3d-projection_1.0-0

