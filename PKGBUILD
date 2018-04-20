# Script generated with Bloom
pkgdesc="ROS - Controller for executing joint-space trajectories on a group of joints."
url='https://github.com/ros-controls/ros_controllers/wiki'

pkgname='ros-lunar-joint-trajectory-controller'
pkgver='0.13.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-angles'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-controller-interface'
'ros-lunar-controller-manager'
'ros-lunar-hardware-interface'
'ros-lunar-realtime-tools'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
'ros-lunar-xacro'
)

depends=('ros-lunar-actionlib'
'ros-lunar-angles'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-controller-interface'
'ros-lunar-hardware-interface'
'ros-lunar-realtime-tools'
'ros-lunar-roscpp'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
)

conflicts=()
replaces=()

_dir=joint_trajectory_controller
source=()
md5sums=()

prepare() {
    cp -R $startdir/joint_trajectory_controller $srcdir/joint_trajectory_controller
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

