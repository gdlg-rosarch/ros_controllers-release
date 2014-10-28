Name:           ros-hydro-joint-trajectory-controller
Version:        0.7.3
Release:        0%{?dist}
Summary:        ROS joint_trajectory_controller package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-angles
Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-control-toolbox
Requires:       ros-hydro-controller-interface
Requires:       ros-hydro-controller-manager
Requires:       ros-hydro-hardware-interface
Requires:       ros-hydro-realtime-tools
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rostest
Requires:       ros-hydro-rqt-plot
Requires:       ros-hydro-trajectory-msgs
Requires:       ros-hydro-urdf
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-catkin >= 0.5.68
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-control-toolbox
BuildRequires:  ros-hydro-controller-interface
BuildRequires:  ros-hydro-controller-manager
BuildRequires:  ros-hydro-hardware-interface
BuildRequires:  ros-hydro-realtime-tools
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-urdf
BuildRequires:  ros-hydro-xacro

%description
Controller for executing joint-space trajectories on a group of joints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Oct 28 2014 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.7.3-0
- Autogenerated by Bloom

