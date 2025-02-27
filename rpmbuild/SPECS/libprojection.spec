# rpmbuild -ba SPECS/libprojection.spec
Name:           libprojection
Version:        1.0
Release:        1%{?dist}
Summary:        Calculated forward and inverse projections
Group:          Unspecified
License:        Public Domain, CC0-1.0
URL:            https://code.usgs.gov/vsc/ash3d/volcano-ash3d-projection
Source0:        volcano-ash3d-projection-master.zip
BuildRequires:  make,gcc-gfortran
#BuildRoot:      /opt/USGS
#Requires:    

%description
libprojection is a fortran 90 module that contain subroutines that can convert between lon,lat and various projections commonly used in numerical weather prediction forecast/reanalysis products.

%prep
rm -rf $RPM_BUILD_DIR/volcano-ash3d-projection-master
unzip $RPM_SOURCE_DIR/volcano-ash3d-projection-master.zip

%build
cd volcano-ash3d-projection-master
make

%install
mkdir -p $RPM_BUILD_ROOT/opt/USGS/lib
mkdir -p $RPM_BUILD_ROOT/opt/USGS/include
cp volcano-ash3d-projection-master/libprojection.a $RPM_BUILD_ROOT/opt/USGS/lib/
cp volcano-ash3d-projection-master/projection.mod $RPM_BUILD_ROOT/opt/USGS/include/

%clean
#rm -rf $RPM_BUILD_ROOT/

%files
/opt/USGS/lib/libprojection.a
/opt/USGS/include/projection.mod

%changelog


