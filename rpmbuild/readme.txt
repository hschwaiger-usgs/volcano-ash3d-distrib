rpmbuild directory need the following sub-directories:
BUILD       : contains the unziped source code from the prep stage
BUILDROOT   : This is the root system where files are installed
RPMS        : final rpms
SOURCES     : stores the source code in tarballs or zip files
SPECS       : contains the .spec files with build instructions
SRPMS       : source rpms

wget https://code.usgs.gov/vsc/ash3d/volcano-ash3d-projection/-/archive/master/volcano-ash3d-projection-master.zip
wget https://code.usgs.gov/vsc/ash3d/volcano-ash3d-hourssince/-/archive/master/volcano-ash3d-hourssince-master.zip
wget https://code.usgs.gov/vsc/ash3d/volcano-ash3d-metreader/-/archive/master/volcano-ash3d-metreader-master.zip
wget https://code.usgs.gov/vsc/ash3d/volcano-ash3d/-/archive/master/volcano-ash3d-master.zip

To build an rpm, type (from rpmbuild):
 rpmbuild -ba --clean SPECS/libhourssince.spec   (-ba indicates to build the binary with all steps)
 
 -bp does just the prep stage
 -bc does the build stage (e.g. make)
 -bi does the install stage (make install)
 -bb builds the rpm binary (after prep, build, install)
 -bs builds the source rpm

