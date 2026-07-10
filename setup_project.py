from pathlib import Path

PROJECT_NAME = "QuantumSecurityFramework"

directories = [
    ".vscode",

    "src/qsbf",
    "src/qsbf/config",
    "src/qsbf/rsa",
    "src/qsbf/aes",
    "src/qsbf/hybrid",
    "src/qsbf/pqc",
    "src/qsbf/fhe",
    "src/qsbf/benchmarking",
    "src/qsbf/visualization",
    "src/qsbf/utils",
    "src/qsbf/reports",

    "configs",

    "data/plaintext",
    "data/encrypted",
    "data/decrypted",
    "data/keys",

    "results/csv",
    "results/excel",
    "results/figures",
    "results/reports",

    "logs",
    "docs",
    "tests",
    "notebooks",
]

files = {

    "README.md": f"# {PROJECT_NAME}\n",

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
*.pyc
*.pyo
*.pyd

# Virtual Environment
.venv/
venv/

# VS Code
.vscode/settings.json

# Jupyter
.ipynb_checkpoints/

# Results
results/

# Logs
logs/

# OS
.DS_Store
Thumbs.db
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

package_dirs = [
    "src/qsbf",
    "src/qsbf/config",
    "src/qsbf/rsa",
    "src/qsbf/aes",
    "src/qsbf/hybrid",
    "src/qsbf/pqc",
    "src/qsbf/fhe",
    "src/qsbf/benchmarking",
    "src/qsbf/visualization",
    "src/qsbf/utils",
    "src/qsbf/reports",
]

for directory in directories:
    Path(directory).mkdir(parents=True, exist_ok=True)

for package in package_dirs:
    init_file = Path(package) / "__init__.py"
    init_file.touch(exist_ok=True)

for filename, content in files.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

sample = Path("data/plaintext/sample.txt")
sample.write_text(
    "This is the sample plaintext used for cryptographic benchmarking.",
    encoding="utf-8"
)

print("=" * 60)
print("Quantum Security Benchmarking Framework created successfully.")
print("=" * 60)