"""
setup_project.py

Quantum Security Benchmarking Framework (QSBF)
Professional Project Generator
"""

from pathlib import Path

PROJECT_NAME = "QuantumSecurityFramework"

# ==========================================================
# Project Directory Structure
# ==========================================================

directories = [

    # VS Code
    ".vscode",

    # Source
    "src",
    "src/qsbf",
    "src/qsbf/config",
    "src/qsbf/core",
    "src/qsbf/rsa",
    "src/qsbf/aes",
    "src/qsbf/hybrid",
    "src/qsbf/pqc",
    "src/qsbf/fhe",
    "src/qsbf/benchmarking",
    "src/qsbf/visualization",
    "src/qsbf/utils",
    "src/qsbf/reports",
    "src/qsbf/fileio",

    # Configuration
    "configs",

    # Data
    "data",
    "data/plaintext",
    "data/encrypted",
    "data/decrypted",
    "data/keys",

    # Results
    "results",
    "results/csv",
    "results/excel",
    "results/figures",
    "results/reports",

    # Others
    "logs",
    "docs",
    "tests",
    "notebooks",
]

# ==========================================================
# Root Files
# ==========================================================

files = {

    "README.md":
f"""# {PROJECT_NAME}

Quantum Security Benchmarking Framework
""",

    "requirements.txt": "",

    "LICENSE": "",

    "main.py":
'''def main():
    print("Quantum Security Benchmarking Framework")


if __name__ == "__main__":
    main()
''',

    ".gitignore":
'''# Python
__pycache__/
*.py[cod]
*.egg-info/

# Virtual Environment
.venv/
venv/

# VS Code
.vscode/settings.json

# Notebook
.ipynb_checkpoints/

# Results
results/

# Logs
logs/

# OS
Thumbs.db
.DS_Store
''',

    "pyproject.toml":
'''[project]
name = "qsbf"
version = "0.1.0"
description = "Quantum Security Benchmarking Framework"
requires-python = ">=3.12"
''',

    ".vscode/settings.json":
'''{
    "python.defaultInterpreterPath": ".venv\\\\Scripts\\\\python.exe",
    "python.analysis.extraPaths": [
        "./src"
    ],
    "editor.formatOnSave": true
}
''',

    ".vscode/launch.json":
'''{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Main",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal"
        }
    ]
}
''',

    ".vscode/tasks.json":
'''{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Main",
            "type": "shell",
            "command": "python main.py",
            "group": "build"
        }
    ]
}
'''
}

# ==========================================================
# Python Module Templates
# ==========================================================

module_templates = {

    "src/qsbf/fileio/file_reader.py":
'''"""
file_reader.py

Utility for reading files.
"""

from pathlib import Path


class FileReader:

    def read(self, file_path):

        path = Path(file_path)

        with open(path, "rb") as f:
            return f.read()
''',

    "src/qsbf/fileio/file_writer.py":
'''"""
file_writer.py

Utility for writing files.
"""

from pathlib import Path


class FileWriter:

    def write(self, file_path, data):

        path = Path(file_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as f:
            f.write(data)
'''
}

# ==========================================================
# Create Directories
# ==========================================================

print("\nCreating directories...")

for directory in directories:

    Path(directory).mkdir(parents=True, exist_ok=True)

# ==========================================================
# Create __init__.py
# ==========================================================

print("Creating packages...")

for directory in directories:

    if directory.startswith("src/"):

        init_file = Path(directory) / "__init__.py"

        if not init_file.exists():
            init_file.touch()

# ==========================================================
# Create Root Files
# ==========================================================

print("Creating project files...")

for filename, content in files.items():

    path = Path(filename)

    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():

        path.write_text(content, encoding="utf-8")

# ==========================================================
# Create Module Templates
# ==========================================================

print("Creating module templates...")

for filename, content in module_templates.items():

    path = Path(filename)

    if not path.exists():

        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(content, encoding="utf-8")

# ==========================================================
# Sample File
# ==========================================================

sample = Path("data/plaintext/sample.txt")

if not sample.exists():

    sample.write_text(
        "This is the sample plaintext used for cryptographic benchmarking.",
        encoding="utf-8",
    )

# ==========================================================
# Completed
# ==========================================================

print("\n" + "=" * 60)
print(" Quantum Security Benchmarking Framework Generated")
print("=" * 60)

print("\nProject Root :")
print(Path.cwd())

print("\nCompleted Successfully.")