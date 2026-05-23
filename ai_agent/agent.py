from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
import requests

MCP_URL = "http://localhost:8000"

@tool
def get_active_nodes() -> str:
    """Get all active ROS2 nodes currently running."""
    try:
        response = requests.get(f"{MCP_URL}/get_active_nodes", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_robot_status() -> str:
    """Get current robot status and active topics."""
    try:
        response = requests.get(f"{MCP_URL}/get_robot_status", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_lidar_snapshot() -> str:
    """Get a snapshot of LiDAR sensor data from /scan topic."""
    try:
        response = requests.get(f"{MCP_URL}/get_lidar_snapshot", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_navigation_status() -> str:
    """Get current navigation and odometry status."""
    try:
        response = requests.get(f"{MCP_URL}/get_navigation_status", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_tf_tree() -> str:
    """Get the TF transformation tree of the robot."""
    try:
        response = requests.get(f"{MCP_URL}/get_tf_tree", timeout=5)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def get_full_health_check() -> str:
    """Get a complete health check of the robot including nodes, topics, lidar and odometry all at once."""
    try:
        response = requests.get(f"{MCP_URL}/get_full_health_check", timeout=15)
        return str(response.json())
    except Exception as e:
        return f"Error: {e}"

# Setup LLM — thinking disabled, fast mode
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    num_predict=256,
    extra_body={"think": False}
)

tools = [
    get_active_nodes,
    get_robot_status,
    get_lidar_snapshot,
    get_navigation_status,
    get_tf_tree,
    get_full_health_check
]

agent = create_react_agent(llm, tools)

def ask_ros2(question: str) -> str:
    """Send a question to the ROS2 AI agent."""
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].content