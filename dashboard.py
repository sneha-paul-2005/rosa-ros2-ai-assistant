import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import streamlit as st
import requests
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ask_ros2 import ask_with_rag

MCP_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="ROS2 AI Troubleshooter",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 ROSA — ROS2 AI Assistant")
st.caption("Your intelligent ROS2 companion — diagnose, fix, and monitor your robot")

# Sidebar — Robot Status
with st.sidebar:
    st.header("🔌 Robot Status")
    if st.button("🔄 Refresh Status"):
        st.rerun()

    try:
        nodes = requests.get(f"{MCP_URL}/get_active_nodes", timeout=5).json()
        topics = requests.get(f"{MCP_URL}/get_robot_status", timeout=5).json()

        node_list = nodes.get("nodes", [])
        topic_list = topics.get("topics", [])

        # Health score
        health = 0
        if node_list and node_list[0]: health += 50
        if topic_list and topic_list[0]: health += 50

        st.metric("Health Score", f"{health}/100")

        if health == 100:
            st.success("Robot Online ✅")
        elif health > 0:
            st.warning("Partial Online ⚠️")
        else:
            st.error("Robot Offline ❌")

        st.subheader("Active Nodes")
        if node_list and node_list[0]:
            for node in node_list:
                st.code(node)
        else:
            st.warning("No nodes found")

        st.subheader("Active Topics")
        if topic_list and topic_list[0]:
            for topic in topic_list:
                st.code(topic)
        else:
            st.warning("No topics found")

    except Exception as e:
        st.error(f"MCP Server not running!\nStart it with:\nuvicorn mcp_server.main:app --port 8000")

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Ask AI",
    "🏥 Health Check",
    "🔧 Code Fixer",
    "📋 Error Log Analyzer"
])

# Tab 1 — Chat
with tab1:
    st.header("💬 Ask the ROS2 AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask anything about your ROS2 robot..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                response = ask_with_rag(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Tab 2 — Health Check
with tab2:
    st.header("🏥 Full Robot Health Check")
    st.caption("Checks all nodes, topics, LiDAR and odometry at once")

    if st.button("🚀 Run Full Health Check"):
        with st.spinner("Checking robot health..."):
            try:
                result = requests.get(f"{MCP_URL}/get_full_health_check", timeout=30).json()
                health = result.get("health_check", {})

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("🔵 Nodes")
                    for node in health.get("nodes", []):
                        st.code(node)

                    st.subheader("📡 Topics")
                    for topic in health.get("topics", []):
                        st.code(topic)

                with col2:
                    st.subheader("📡 LiDAR")
                    lidar = health.get("lidar", "No data")
                    if "inf" in lidar:
                        st.info("LiDAR working — no obstacles detected (inf values are normal in empty world)")
                    else:
                        st.success("LiDAR detecting obstacles!")
                    st.text(lidar[:300])

                    st.subheader("🧭 Odometry")
                    st.text(health.get("odometry", "No data")[:300])

            except Exception as e:
                st.error("MCP Server not running!")

# Tab 3 — Code Fixer
with tab3:
    st.header("🔧 ROS2 Code Fixer")
    st.caption("Paste your broken ROS2 code and AI will fix it")

    broken_code = st.text_area(
        "Paste your broken code here:",
        height=200,
        placeholder="# Paste your broken ROS2 code here..."
    )

    if st.button("🔧 Fix My Code") and broken_code:
        with st.spinner("🤖 Analyzing and fixing code..."):
            question = f"""Fix this broken ROS2 code and explain what was wrong:

```python
{broken_code}
```

Provide the corrected code and explain the fixes."""
            response = ask_with_rag(question)

        st.subheader("✅ AI Response:")
        st.markdown(response)

# Tab 4 — Error Log Analyzer
with tab4:
    st.header("📋 Error Log Analyzer")
    st.caption("Paste your ROS2 error logs and AI will explain what went wrong")

    error_log = st.text_area(
        "Paste your error log here:",
        height=200,
        placeholder="Paste your ROS2 error or log output here..."
    )

    if st.button("🔍 Analyze Error") and error_log:
        with st.spinner("🤖 Analyzing error..."):
            question = f"""Analyze this ROS2 error log and tell me:
1. What went wrong
2. Why it happened  
3. How to fix it with exact commands

Error log:
{error_log}"""
            response = ask_with_rag(question)

        st.subheader("✅ Analysis:")
        st.markdown(response)