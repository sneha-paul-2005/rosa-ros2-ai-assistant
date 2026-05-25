#!/usr/bin/env python3
import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_agent.agent import ask_ros2
from rag.rag_engine import search_ros2_knowledge

def ask_with_rag(question: str) -> str:
    knowledge = search_ros2_knowledge(question)
    enhanced_question = f"""User question: {question}

Relevant knowledge base information:
{knowledge}

Use the above knowledge base information to help answer. Also check live robot data if needed."""
    return ask_ros2(enhanced_question)

def main():
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print(f"\n🤖 Thinking...\n")
        response = ask_with_rag(question)
        print(f"💡 {response}\n")
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
                response = ask_with_rag(question)
                print(f"💡 {response}\n")
            except KeyboardInterrupt:
                print("\nGoodbye! 🚀")
                break

if __name__ == "__main__":
    main()
    