from agent import CodeReviewAgent


def main():
    agent = CodeReviewAgent()

    print("=" * 60)
    print("Code Review Agent")
    print("=" * 60)
    print("Input a code file name, for example: test.py")
    print("After review, you can ask follow-up questions.")
    print("Type exit to quit.")
    print("=" * 60)

    code_extensions = (
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".c",
        ".html",
        ".css",
    )

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("\nAgent: Goodbye!")
            break

        if not user_input:
            continue

        try:
            if user_input.lower().endswith(code_extensions):

                print("\n[Agent] File detected.")
                result = agent.review_file(user_input)

            else:

                print("\n[Agent] Using conversation memory.")
                result = agent.chat(user_input)

            print("\nAgent:")
            print(result)

        except Exception as e:

            print("\nUnexpected Error:")
            print(e)


if __name__ == "__main__":
    main()