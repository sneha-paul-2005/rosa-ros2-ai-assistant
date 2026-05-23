#!/usr/bin/env python3
import sys
import os

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_agent.agent import ask_ros2

def main():
    # If question passed as argument
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print(f"\n🤖 Thinking...\n")
        response = ask_ros2(question)
        print(f"💡 {response}\n")

    # Interactive mode
    else:
        print("\n🤖 ROS2 AI Troubleshooter")
        print("=" * 40)
        print("Type your question or 'exit' to quit\n")

        while True:
            try:
                question = input("You: ").strip()
                if question.lower() in ["exit", "quit", "q"]:
                    print("Goodbye! 🚀")
                    break
                if not question:
                    continue
                print("\n🤖 Thinking...\n")
                response = ask_ros2(question)
                print(f"💡 {response}\n")
            except KeyboardInterrupt:
                print("\nGoodbye! 🚀")
                break

if __name__ == "__main__":
    main()