#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/nickolay/demonstration/src/executive_smach/smach"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/nickolay/demonstration/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/nickolay/demonstration/install/lib/python3/dist-packages:/home/nickolay/demonstration/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/nickolay/demonstration/build" \
    "/usr/bin/python3" \
    "/home/nickolay/demonstration/src/executive_smach/smach/setup.py" \
    egg_info --egg-base /home/nickolay/demonstration/build/executive_smach/smach \
    build --build-base "/home/nickolay/demonstration/build/executive_smach/smach" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/nickolay/demonstration/install" --install-scripts="/home/nickolay/demonstration/install/bin"
