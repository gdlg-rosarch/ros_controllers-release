Name:           ros-indigo-gripper-action-controller
Version:        0.9.1
Release:        0%{?dist}
Summary:        ROS gripper_action_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-angles
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-control-toolbox
Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-control-toolbox
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
The gripper_action_controller package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Nov 03 2014 Sachin Chitta <robot.moveit@gmail.com> - 0.9.1-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Sachin Chitta <robot.moveit@gmail.com> - 0.9.0-0
- Autogenerated by Bloom

