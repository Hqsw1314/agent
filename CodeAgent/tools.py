from pathlib import Path


def read_code_file(file_path: str) -> str:
    try:
        path = Path(file_path)

        if not path.exists():
            return "Error: file does not exist."

        if not path.is_file():
            return "Error: path is not a file."

        allowed_extensions = {
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".html",
            ".css",
        }

        if path.suffix.lower() not in allowed_extensions:
            return "Error: unsupported file type."

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return f"Error reading file: {str(e)}"