# Script generated with Bloom
pkgdesc="ROS - Library of ros controllers"
url='http://ros.org/wiki/ros_controllers'

pkgname='ros-lunar-ros-controllers'
pkgver='0.13.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-diff-drive-controller'
'ros-lunar-effort-controllers'
'ros-lunar-force-torque-sensor-controller'
'ros-lunar-forward-command-controller'
'ros-lunar-gripper-action-controller'
'ros-lunar-imu-sensor-controller'
'ros-lunar-joint-state-controller'
'ros-lunar-joint-trajectory-controller'
'ros-lunar-position-controllers'
'ros-lunar-rqt-joint-trajectory-controller'
'ros-lunar-velocity-controllers'
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

