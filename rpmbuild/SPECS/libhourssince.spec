# rpmbuild -ba SPECS/libhourssince.spec
Name:           libhourssince
Version:        1.0
Release:        1%{?dist}
Summary:        Time difference calculator
Group:          Unspecified
License:        Public Domain, CC0-1.0
URL:            https://code.usgs.gov/vsc/ash3d/volcano-ash3d-hourssince
Source0:        volcano-ash3d-hourssince-master.zip
BuildRequires:  make,gcc-gfortran
#BuildRoot:      /opt/USGS
#Requires:    

%description
libhourssince is a collection of functions and subroutines that calculate the number of hours of a given calendar date from Jan. 1 of a reference year.

%prep
rm -rf $RPM_BUILD_DIR/volcano-ash3d-hourssince-master
unzip $RPM_SOURCE_DIR/volcano-ash3d-hourssince-master.zip

%build
cd volcano-ash3d-hourssince-master
make

%install
mkdir -p $RPM_BUILD_ROOT/opt/USGS/lib
cp volcano-ash3d-hourssince-master/libhourssince.a $RPM_BUILD_ROOT/opt/USGS/lib/

%clean
#rm -rf $RPM_BUILD_ROOT/

%files
/opt/USGS/lib/libhourssince.a

%changelog


