# rpmbuild -ba SPECS/ash3d.spec
Name:           ash3d
Version:        1.0
Release:        1%{?dist}
Summary:        Volcanic ash dispersion, transport and deposition model
Group:          Unspecified
License:        Public Domain, CC0-1.0
URL:            https://code.usgs.gov/vsc/ash3d/volcano-ash3d
Source0:        volcano-ash3d-master.zip
BuildRequires:  make,gcc-gfortran,netcdf,eccodes,libhourssince,libprojection,libmetreader
#BuildRoot:      /opt/USGS
#Requires:    

%description
Ash3d is a numerical model for calculating the transport and deposition of volcanic ash.

%prep
rm -rf $RPM_BUILD_DIR/volcano-ash3d-master
unzip $RPM_SOURCE_DIR/volcano-ash3d-master.zip

%build
cd volcano-ash3d-master/src
make

%install
mkdir -p $RPM_BUILD_ROOT/opt/USGS/Ash3d/bin/tools
mkdir -p $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/
cp volcano-ash3d-master/bin/Ash3d                          $RPM_BUILD_ROOT/opt/USGS/Ash3d/bin/
cp volcano-ash3d-master/bin/Ash3d_PostProc                 $RPM_BUILD_ROOT/opt/USGS/Ash3d/bin/
cp volcano-ash3d-master/bin/tools/Ash3d_ASCII_check        $RPM_BUILD_ROOT/opt/USGS/Ash3d/bin/tools/
cp volcano-ash3d-master/share/GlobalAirports_ewert.txt     $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/
cp volcano-ash3d-master/share/VotW_ESP_v12_csv.txt         $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/
cp volcano-ash3d-master/share/post_proc/CloudLoad_hsv.png  $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/
cp volcano-ash3d-master/share/post_proc/logo.png           $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/
cp volcano-ash3d-master/share/post_proc/USGSvid.png        $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/
cp volcano-ash3d-master/share/post_proc/USGS_warning3.png  $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/
cp volcano-ash3d-master/share/post_proc/world_cities.txt   $RPM_BUILD_ROOT/opt/USGS/Ash3d/share/post_proc/

%clean
#rm -rf $RPM_BUILD_ROOT/

%files
/opt/USGS/Ash3d/bin/Ash3d
/opt/USGS/Ash3d/bin/Ash3d_PostProc
/opt/USGS/Ash3d/bin/tools/Ash3d_ASCII_check
/opt/USGS/Ash3d/share/GlobalAirports_ewert.txt
/opt/USGS/Ash3d/share/VotW_ESP_v12_csv.txt
/opt/USGS/Ash3d/share/post_proc/CloudLoad_hsv.png
/opt/USGS/Ash3d/share/post_proc/logo.png
/opt/USGS/Ash3d/share/post_proc/USGSvid.png
/opt/USGS/Ash3d/share/post_proc/USGS_warning3.png
/opt/USGS/Ash3d/share/post_proc/world_cities.txt

%changelog


