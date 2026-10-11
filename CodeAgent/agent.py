import os
import time
from openai import OpenAI
from dotenv import load_dotenv

from tools import read_code_file

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

SYSTEM_PROMPT = """
You are a professional Code Review Agent.

Your tasks:
1. Explain what the code does.
2. Find bugs and potential exceptions.
3. Analyze edge cases.
4. Give concrete improvement suggestions.
5. Provide improved code when appropriate.
6. Remember previous conversation context.

Reply in Chinese.

Use this structure when reviewing code:

[Code Function]

[Potential Problems]

[Improvement Suggestions]

[Improved Code]
"""


class CodeReviewAgent:

    def __init__(self):
        self.history = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def call_llm(self, messages, retries=3):
        for attempt in range(retries):
            try:
                response = client.chat.completions.create(
                    model="qwen-plus",
                    messages=messages
                )

                return response.choices[0].message.content

            except Exception as e:
                if attempt < retries - 1:
                    print(
                        f"API call failed. Retrying "
                        f"{attempt + 1}/{retries}..."
                    )
                    time.sleep(2)
                else:
                    return f"API Error: {str(e)}"

    def review_file(self, file_path):
        print(f"[Agent] Reading file: {file_path}")

        code = read_code_file(file_path)

        if code.startswith("Error:"):
            return code

        print("[Agent] File reading tool completed.")
        print("[Agent] Sending code to LLM...")

        user_message = f"""
Review this file:

File:
{file_path}

Code:
{code}
"""

        self.history.append({
            "role": "user",
            "content": user_message
        })

        answer = self.call_llm(self.history)

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    def chat(self, question):
        self.history.append({
            "role": "user",
            "content": question
        })

        answer = self.call_llm(self.history)

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer