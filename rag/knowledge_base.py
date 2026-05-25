# ROS2 Knowledge Base — Comprehensive errors and fixes

ROS2_KNOWLEDGE = [
    # --- GENERAL ROS2 ---
    {
        "topic": "Node not found",
        "content": "If a ROS2 node is not found, make sure the package is built with colcon build and the workspace is sourced with source install/setup.bash. Also check if the node is running with ros2 node list."
    },
    {
        "topic": "ROS2 environment not set up",
        "content": "If ROS2 commands are not found, source the ROS2 setup file with source /opt/ros/jazzy/setup.bash. Add it to ~/.bashrc to make it permanent. For ROS2 Jazzy specifically use the jazzy path."
    },
    {
        "topic": "Colcon build failed",
        "content": "If colcon build fails, check for missing dependencies with rosdep install --from-paths src --ignore-src -r -y. Make sure you are in the workspace root directory. Check for Python syntax errors in your code."
    },
    {
        "topic": "Package not found",
        "content": "If a ROS2 package is not found, install it with sudo apt install ros-jazzy-package-name. Source the workspace after installation. Use ros2 pkg list to see all available packages."
    },
    {
        "topic": "Topic not publishing",
        "content": "If a topic is not publishing, use ros2 topic list to check if it exists. Use ros2 topic hz /topic_name to check publish rate. Use ros2 topic echo /topic_name to see messages. Check the node publishing it is running."
    },
    {
        "topic": "ROS2 node crashes immediately",
        "content": "If a ROS2 node crashes immediately, check the error logs with ros2 run package node --ros-args --log-level DEBUG. Look for missing parameters or incorrect topic names. Check if required dependencies are running."
    },
    {
        "topic": "ROS2 service not available",
        "content": "If a ROS2 service is not available, check running services with ros2 service list. Make sure the node providing the service is running. Try calling it with ros2 service call /service_name service_type."
    },
    {
        "topic": "ROS2 parameter not set",
        "content": "If a ROS2 parameter is not set, use ros2 param list to see all parameters. Set a parameter with ros2 param set /node_name param_name value. Check the node's default parameters in its source code."
    },
    {
        "topic": "ROS2 bag recording issues",
        "content": "If ros2 bag record is not working, make sure the topics exist with ros2 topic list. Record specific topics with ros2 bag record -o bag_name /topic1 /topic2. Check available disk space before recording."
    },
    {
        "topic": "ROS2 launch file not found",
        "content": "If a launch file is not found, make sure the package is built and sourced. Check the launch file path with ros2 pkg prefix package_name. Rebuild with colcon build --packages-select package_name."
    },

    # --- TURTLEBOT3 ---
    {
        "topic": "TurtleBot3 not moving",
        "content": "If TurtleBot3 is not moving, check that TURTLEBOT3_MODEL is set with export TURTLEBOT3_MODEL=burger. Make sure teleop node is running with ros2 run turtlebot3_teleop teleop_keyboard. Check /cmd_vel topic has a publisher."
    },
    {
        "topic": "TurtleBot3 model not set",
        "content": "TurtleBot3 requires the model environment variable to be set. Run export TURTLEBOT3_MODEL=burger for Burger model or export TURTLEBOT3_MODEL=waffle for Waffle model. Add it to ~/.bashrc to make it permanent."
    },
    {
        "topic": "TurtleBot3 package not found",
        "content": "If TurtleBot3 packages are not found, install them with sudo apt install ros-jazzy-turtlebot3 ros-jazzy-turtlebot3-gazebo ros-jazzy-turtlebot3-navigation2. Source ROS2 after installation."
    },
    {
        "topic": "TurtleBot3 teleop not working",
        "content": "If TurtleBot3 teleop is not working, run ros2 run turtlebot3_teleop teleop_keyboard. Make sure the terminal window with teleop is focused when pressing keys. Check that /cmd_vel topic is being published."
    },
    {
        "topic": "TurtleBot3 URDF not loading",
        "content": "If TurtleBot3 URDF is not loading, check that robot_state_publisher is running. Verify TURTLEBOT3_MODEL is set correctly. Make sure turtlebot3_description package is installed."
    },

    # --- GAZEBO ---
    {
        "topic": "Gazebo not launching",
        "content": "If Gazebo fails to launch, source ROS2 setup with source /opt/ros/jazzy/setup.bash. Check that turtlebot3_gazebo package is installed. Try killing old Gazebo processes with pkill -f gazebo."
    },
    {
        "topic": "Gazebo world not loading",
        "content": "If Gazebo world is not loading, check that the world file exists. Set the correct world path in the launch file. Try launching with a simple empty world first to isolate the issue."
    },
    {
        "topic": "Gazebo robot not spawning",
        "content": "If the robot is not spawning in Gazebo, check that the URDF is valid. Make sure the spawn_entity node is running. Check Gazebo logs for spawn errors. Try respawning with ros2 run gazebo_ros spawn_entity.py."
    },
    {
        "topic": "Gazebo and ROS2 not communicating",
        "content": "If Gazebo and ROS2 are not communicating, check that ros_gz_bridge is running. Verify the bridge topics are correctly mapped. Make sure ros-jazzy-ros-gz-bridge package is installed."
    },
    {
        "topic": "Gazebo simulation running slow",
        "content": "If Gazebo simulation is running slowly, reduce the simulation complexity. Close unnecessary applications to free RAM. Lower the physics update rate in the world file. Consider using a lighter robot model."
    },
    {
        "topic": "Gazebo crash on startup",
        "content": "If Gazebo crashes on startup, update GPU drivers. Try running with software rendering: export LIBGL_ALWAYS_SOFTWARE=1. Kill existing Gazebo processes with pkill -f gz. Clear Gazebo cache with rm -rf ~/.gz."
    },

    # --- LIDAR ---
    {
        "topic": "LiDAR showing inf values",
        "content": "LiDAR showing inf values means no obstacles are detected in sensor range. This is normal in an empty Gazebo world. The sensor is working correctly. Add obstacles in Gazebo to see real range values."
    },
    {
        "topic": "LiDAR not publishing",
        "content": "If LiDAR is not publishing on /scan topic, check that the robot is spawned in Gazebo. Verify ros_gz_bridge is running and bridging the scan topic. Check with ros2 topic hz /scan to see publish rate."
    },
    {
        "topic": "LiDAR data incorrect",
        "content": "If LiDAR data seems incorrect, check the sensor configuration in the URDF. Verify the scan range parameters like range_min and range_max. Make sure the sensor frame is correctly defined in TF tree."
    },
    {
        "topic": "LiDAR scan frequency too low",
        "content": "If LiDAR scan frequency is too low, check the sensor update rate in URDF or SDF file. Increase the update_rate parameter. Make sure the simulation is not running slower than real time."
    },

    # --- NAVIGATION ---
    {
        "topic": "Nav2 navigation not working",
        "content": "If Nav2 is not working, make sure to launch navigation with ros2 launch nav2_bringup navigation_launch.py. Check that the map is provided and amcl localization is running. Verify /scan and /odom topics are publishing."
    },
    {
        "topic": "Nav2 goal rejected",
        "content": "If Nav2 rejects a navigation goal, check that the goal is within the map bounds. Make sure the robot is localized correctly with AMCL. Verify the costmap is properly configured. Check Nav2 logs for specific error."
    },
    {
        "topic": "Nav2 robot stuck during navigation",
        "content": "If robot gets stuck during navigation, check for obstacles in the costmap. Clear the costmap with ros2 service call /clear_costmaps. Adjust the recovery behaviors in Nav2 parameters. Check inflation radius settings."
    },
    {
        "topic": "Nav2 map not loading",
        "content": "If Nav2 map is not loading, check the map file path in the launch file. Make sure the map yaml file and pgm file are in the same directory. Verify map_server node is running with ros2 node list."
    },
    {
        "topic": "AMCL localization not working",
        "content": "If AMCL localization is not working, make sure the map is loaded. Check that /scan topic is publishing. Set initial pose in RViz or with ros2 topic pub. Increase the number of particles in AMCL parameters."
    },
    {
        "topic": "Nav2 costmap not updating",
        "content": "If Nav2 costmap is not updating, check that sensor topics are publishing. Verify costmap parameters include correct sensor sources. Make sure observation sources are correctly configured in nav2_params.yaml."
    },

    # --- TF AND TRANSFORMS ---
    {
        "topic": "TF tree empty or missing transforms",
        "content": "If TF tree is empty, check that robot_state_publisher is running. Make sure the URDF is loaded correctly. Source the workspace and relaunch. Use ros2 run tf2_tools view_frames to visualize the TF tree."
    },
    {
        "topic": "TF transform lookup failed",
        "content": "If TF transform lookup fails, check that both frames exist in the TF tree. Make sure robot_state_publisher and any static transform publishers are running. Check for timing issues with ros2 run tf2_tools tf2_echo frame1 frame2."
    },
    {
        "topic": "TF extrapolation error",
        "content": "If you see TF extrapolation errors, check for clock synchronization issues. Make sure /clock topic is publishing in simulation. Set use_sim_time to true for all nodes in simulation with --ros-args -p use_sim_time:=true."
    },

    # --- ODOMETRY ---
    {
        "topic": "Odometry not updating",
        "content": "If odometry is not updating, check that the robot simulation is running in Gazebo. Verify /odom topic is publishing with ros2 topic hz /odom. Make sure ros_gz_bridge is running to bridge Gazebo and ROS2 topics."
    },
    {
        "topic": "Odometry drift",
        "content": "Odometry drift is normal over time due to accumulated errors. Use AMCL or other localization methods to correct drift. Consider using sensor fusion with IMU data using robot_localization package."
    },
    {
        "topic": "Robot position not accurate",
        "content": "If robot position is not accurate, check odometry calibration. Use AMCL for map-based localization. Verify wheel encoder parameters in the robot configuration. Consider using external localization sensors."
    },

    # --- GENERAL ROBOT ISSUES ---
    {
        "topic": "Robot stuck or not responding",
        "content": "If the robot is stuck, check active nodes with ros2 node list. Restart the simulation by killing and relaunching Gazebo. Check if /cmd_vel has active publishers. Try sending manual velocity commands with ros2 topic pub."
    },
    {
        "topic": "cmd_vel not working",
        "content": "If /cmd_vel commands are not working, check that the robot controller is running. Verify the topic name matches what the robot expects. Make sure velocity values are within the robot's limits. Check for any emergency stop signals."
    },
    {
        "topic": "IMU data not publishing",
        "content": "If IMU data is not publishing on /imu topic, check that the IMU sensor is defined in the robot URDF. Verify ros_gz_bridge is bridging the IMU topic. Check with ros2 topic hz /imu to see publish rate."
    },
    {
        "topic": "Joint states not publishing",
        "content": "If joint states are not publishing, check that joint_state_publisher is running. Verify the robot URDF has correctly defined joints. Make sure robot_state_publisher is also running alongside joint_state_publisher."
    },
    {
        "topic": "Robot description not loaded",
        "content": "If robot description is not loaded, check that robot_state_publisher is running with the correct URDF. Verify /robot_description topic is publishing. Make sure the URDF file path is correct in the launch file."
    },

    # --- RVIZ ---
    {
        "topic": "RViz not showing robot",
        "content": "If RViz is not showing the robot, check that robot_state_publisher is running. Set the Fixed Frame to odom or map in RViz. Add a RobotModel display and set the topic to /robot_description."
    },
    {
        "topic": "RViz no map displayed",
        "content": "If RViz is not showing the map, check that map_server is running. Add a Map display in RViz and set the topic to /map. Make sure the map file is loaded correctly by Nav2."
    },
    {
        "topic": "RViz laser scan not visible",
        "content": "If laser scan is not visible in RViz, add a LaserScan display and set topic to /scan. Check the Fixed Frame matches the scan frame_id. Make sure the LiDAR is publishing data."
    },

    # --- PERFORMANCE ---
    {
        "topic": "High CPU usage in ROS2",
        "content": "If ROS2 is using high CPU, check for nodes publishing at very high frequencies. Reduce publish rates where possible. Use ros2 topic hz to monitor frequencies. Consider using composable nodes to reduce overhead."
    },
    {
        "topic": "High memory usage",
        "content": "If memory usage is high, check for memory leaks in custom nodes. Reduce the number of running nodes. Lower the history depth of subscriptions. Consider using a lighter simulation or robot model."
    },
    {
        "topic": "Simulation time vs real time",
        "content": "In Gazebo simulation, always use use_sim_time:=true for all nodes. Set the clock source to Gazebo. Make sure /clock topic is being published by Gazebo and bridged to ROS2."
    },
]