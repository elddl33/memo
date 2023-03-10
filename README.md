# memo
```
https://github.com/addpipe/simple-recorderjs-demo
```

# first
```
sudo apt autoremove

sudo apt updatecatkin_create_pkg smart rospy roscpp std_msgs
sudo apt upgrade

sudo apt install terminator

sudo apt install thonny
```

# install ROS
```
sudo apt update
sudo apt upgrade

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-get update
sudo apt-get install ros-melodic-desktop-full
sudo apt-get install python-rosdep
sudo rosdep init
rosdep update
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

sudo apt-get install python-catkin-tools
```
```
mkdir -p ~/catkin_ws/srccatkin_make
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin buildcatkin_create_pkg smart rospy roscpp std_msgs
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
```
//in bashrc
//if Wifi = smart2.4G
export ROS_HOSTNAME=192.168.0.141
export ROS_MASTER_URI=htcatkin_maketp://192.168.0.141:11311
```

# make ros package
```
//catkin_create_pkg <package_name> [dependencies]
cd ~/catkin_ws/src
catkin_create_pkg smart rospy roscpp std_msgs
cd ~/catkin_ws
//delete bulid and devel files in catkin_ws
catkin_make
```

