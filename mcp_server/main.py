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