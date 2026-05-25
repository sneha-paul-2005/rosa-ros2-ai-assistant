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

    # Detect if it's a code fixing request
    code_keywords = ["fix", "error", "broken", "wrong", "correct", "debug"]
    is_code_request = any(word in question.lower() for word in code_keywords)

    if is_code_request:
        enhanced_question = f"""You are a ROS2 code expert. The user wants you to fix their code.

User request: {question}

Relevant knowledge:
{knowledge}

IMPORTANT: Focus on fixing the code only. Do NOT check live robot data.
Show the corrected code and explain each fix clearly."""
    else:
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