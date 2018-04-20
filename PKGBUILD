# Script generated with Bloom
pkgdesc="ROS - velocity_controllers"
url='https://github.com/ros-controls/ros_controllers/wiki'

pkgname='ros-kinetic-velocity-controllers'
pkgver='0.13.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-control-toolbox'
'ros-kinetic-controller-interface'
'ros-kinetic-forward-command-controller'
'ros-kinetic-realtime-tools'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-angles'
'ros-kinetic-control-msgs'
'ros-kinetic-control-toolbox'
'ros-kinetic-controller-interface'
'ros-kinetic-forward-command-controller'
'ros-kinetic-realtime-tools'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=velocity_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/velocity_controllers $srcdir/velocity_controllers
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

