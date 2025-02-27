# rpmbuild -ba SPECS/libmetreader.spec
Name:           libmetreader
Version:        1.0
Release:        1%{?dist}
Summary:        Interface with NWP data
Group:          Unspecified
License:        Public Domain, CC0-1.0
URL:            https://code.usgs.gov/vsc/ash3d/volcano-ash3d-metreader
Source0:        volcano-ash3d-metreader-master.zip
BuildRequires:  make,gcc-gfortran,netcdf,eccodes,libhourssince,libprojection
#BuildRoot:      /opt/USGS
#Requires:    

%description
libmetreader is a library written in fortran 90 that provides an interface to numerical weather prediction (NWP) data, or other forms of meteorological data, such as radiosonde or other 1-d data.

%prep
rm -rf $RPM_BUILD_DIR/volcano-ash3d-metreader-master
unzip $RPM_SOURCE_DIR/volcano-ash3d-metreader-master.zip

%build
cd volcano-ash3d-metreader-master
make

%install
mkdir -p $RPM_BUILD_ROOT/opt/USGS/lib
mkdir -p $RPM_BUILD_ROOT/opt/USGS/include
mkdir -p $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts
cp volcano-ash3d-metreader-master/libMetReader.a                                   $RPM_BUILD_ROOT/opt/USGS/lib/
cp volcano-ash3d-metreader-master/metreader.mod                                    $RPM_BUILD_ROOT/opt/USGS/include/
cp volcano-ash3d-metreader-master/bin/MetRegrid                                    $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MetSonde                                     $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MetTraj_F                                    $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MetTraj_B                                    $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MetCheck                                     $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/makegfsncml                                  $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/gen_GRIB_index                               $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MetProbe                                     $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/bin/MR_ASCII_check                               $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/tools/GMT_plot_traj.sh                           $RPM_BUILD_ROOT/opt/USGS/bin/
cp volcano-ash3d-metreader-master/autorun_scripts/autorun_gfs.sh                   $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/autorun_nam.sh                   $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/autorun_NCEP_50YearReanalysis.sh $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/get_gfs.sh                       $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/get_nam.sh                       $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/get_NCEP_50YearReanalysis.sh     $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/convert_gfs.sh                   $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/grib2nc.sh                       $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/prune_windfiles.sh               $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/get_gmao.sh                      $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/
cp volcano-ash3d-metreader-master/autorun_scripts/probe_volc.sh                    $RPM_BUILD_ROOT/opt/USGS/bin/autorun_scripts/

%clean
#rm -rf $RPM_BUILD_ROOT/

%files
/opt/USGS/lib/libMetReader.a
/opt/USGS/include/metreader.mod
/opt/USGS/bin/MetRegrid
/opt/USGS/bin/MetSonde
/opt/USGS/bin/MetTraj_F
/opt/USGS/bin/MetTraj_B
/opt/USGS/bin/MetCheck
/opt/USGS/bin/makegfsncml
/opt/USGS/bin/gen_GRIB_index
/opt/USGS/bin/MetProbe
/opt/USGS/bin/MR_ASCII_check
/opt/USGS/bin/GMT_plot_traj.sh
/opt/USGS/bin/autorun_scripts/autorun_gfs.sh
/opt/USGS/bin/autorun_scripts/autorun_nam.sh
/opt/USGS/bin/autorun_scripts/autorun_NCEP_50YearReanalysis.sh
/opt/USGS/bin/autorun_scripts/get_gfs.sh
/opt/USGS/bin/autorun_scripts/get_nam.sh
/opt/USGS/bin/autorun_scripts/get_NCEP_50YearReanalysis.sh
/opt/USGS/bin/autorun_scripts/convert_gfs.sh
/opt/USGS/bin/autorun_scripts/grib2nc.sh
/opt/USGS/bin/autorun_scripts/prune_windfiles.sh
/opt/USGS/bin/autorun_scripts/get_gmao.sh
/opt/USGS/bin/autorun_scripts/probe_volc.sh

%changelog


