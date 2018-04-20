# Script generated with Bloom
pkgdesc="ROS - Library of ros controllers"
url='http://ros.org/wiki/ros_controllers'

pkgname='ros-kinetic-ros-controllers'
pkgver='0.13.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-diff-drive-controller'
'ros-kinetic-effort-controllers'
'ros-kinetic-force-torque-sensor-controller'
'ros-kinetic-forward-command-controller'
'ros-kinetic-gripper-action-controller'
'ros-kinetic-imu-sensor-controller'
'ros-kinetic-joint-state-controller'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-position-controllers'
'ros-kinetic-rqt-joint-trajectory-controller'
'ros-kinetic-velocity-controllers'
)

conflicts=()
replaces=()

_dir=ros_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_controllers $srcdir/ros_controllers
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

