# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nickolay/demonstration/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nickolay/demonstration/build

# Utility rule file for run_tests_smach_ros_rostest_test_state_machine.test.

# Include the progress variables for this target.
include executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/progress.make

executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test:
	cd /home/nickolay/demonstration/build/executive_smach/smach_ros && ../../catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/catkin/cmake/test/run_tests.py /home/nickolay/demonstration/build/test_results/smach_ros/rostest-test_state_machine.xml "/usr/bin/python3 /opt/ros/noetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/nickolay/demonstration/src/executive_smach/smach_ros --package=smach_ros --results-filename test_state_machine.xml --results-base-dir \"/home/nickolay/demonstration/build/test_results\" /home/nickolay/demonstration/src/executive_smach/smach_ros/test/state_machine.test "

run_tests_smach_ros_rostest_test_state_machine.test: executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test
run_tests_smach_ros_rostest_test_state_machine.test: executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/build.make

.PHONY : run_tests_smach_ros_rostest_test_state_machine.test

# Rule to build all files generated by this target.
executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/build: run_tests_smach_ros_rostest_test_state_machine.test

.PHONY : executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/build

executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/clean:
	cd /home/nickolay/demonstration/build/executive_smach/smach_ros && $(CMAKE_COMMAND) -P CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/cmake_clean.cmake
.PHONY : executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/clean

executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/depend:
	cd /home/nickolay/demonstration/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nickolay/demonstration/src /home/nickolay/demonstration/src/executive_smach/smach_ros /home/nickolay/demonstration/build /home/nickolay/demonstration/build/executive_smach/smach_ros /home/nickolay/demonstration/build/executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : executive_smach/smach_ros/CMakeFiles/run_tests_smach_ros_rostest_test_state_machine.test.dir/depend

