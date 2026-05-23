from fastapi import FastAPI
import subprocess
import datetime

app = FastAPI(title="ROS2 MCP Server")

@app.get("/")
def root():
    return {"status": "MCP Server running", "time": str(datetime.datetime.now())}

@app.get("/get_active_nodes")
def get_active_nodes():
    try:
        result = subprocess.run(
            ["ros2", "node", "list"],
            capture_output=True, text=True, timeout=5
        )
        nodes = result.stdout.strip().split("\n")
        return {"nodes": nodes}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_ros_logs")
def get_ros_logs():
    try:
        result = subprocess.run(
            ["journalctl", "-u", "ros2", "-n", "50", "--no-pager"],
            capture_output=True, text=True, timeout=5
        )
        return {"logs": result.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_robot_status")
def get_robot_status():
    try:
        result = subprocess.run(
            ["ros2", "topic", "list"],
            capture_output=True, text=True, timeout=5
        )
        topics = result.stdout.strip().split("\n")
        return {"topics": topics, "status": "online" if topics else "offline"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_lidar_snapshot")
def get_lidar_snapshot():
    try:
        result = subprocess.run(
            ["ros2", "topic", "echo", "--once", "--timeout", "3", "/scan"],
            capture_output=True, text=True, timeout=5
        )
        if result.stdout.strip():
            return {"lidar_data": result.stdout.strip()[:500]}
        else:
            return {"lidar_data": "No data received from /scan topic"}
    except subprocess.TimeoutExpired:
        return {"lidar_data": "Timeout — /scan topic not responding"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_navigation_status")
def get_navigation_status():
    try:
        result = subprocess.run(
            ["ros2", "topic", "echo", "--once", "--timeout", "3", "/odom"],
            capture_output=True, text=True, timeout=5
        )
        if result.stdout.strip():
            return {"navigation_data": result.stdout.strip()[:500]}
        else:
            return {"navigation_data": "No data received from /odom topic"}
    except subprocess.TimeoutExpired:
        return {"navigation_data": "Timeout — /odom topic not responding"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_tf_tree")
def get_tf_tree():
    try:
        result = subprocess.run(
            ["ros2", "run", "tf2_tools", "view_frames"],
            capture_output=True, text=True, timeout=5
        )
        return {"tf_tree": result.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_full_health_check")
def get_full_health_check():
    try:
        # Get nodes
        nodes_result = subprocess.run(
            ["ros2", "node", "list"],
            capture_output=True, text=True, timeout=5
        )
        nodes = nodes_result.stdout.strip().split("\n")

        # Get topics
        topics_result = subprocess.run(
            ["ros2", "topic", "list"],
            capture_output=True, text=True, timeout=5
        )
        topics = topics_result.stdout.strip().split("\n")

        # Get lidar
        lidar_result = subprocess.run(
            ["ros2", "topic", "echo", "--once", "--timeout", "3", "/scan"],
            capture_output=True, text=True, timeout=5
        )
        lidar = lidar_result.stdout.strip()[:300] if lidar_result.stdout.strip() else "No lidar data"

        # Get odom
        odom_result = subprocess.run(
            ["ros2", "topic", "echo", "--once", "--timeout", "3", "/odom"],
            capture_output=True, text=True, timeout=5
        )
        odom = odom_result.stdout.strip()[:300] if odom_result.stdout.strip() else "No odom data"

        return {
            "health_check": {
                "nodes": nodes,
                "topics": topics,
                "lidar": lidar,
                "odometry": odom,
                "status": "online" if nodes else "offline"
            }
        }
    except Exception as e:
        return {"error": str(e)}