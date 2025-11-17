import ast
import os

# 📌 Start scanning from the current folder (project root)
base_path = "."

print("\n🔎 Scanning all Python files for Functions & Classes...\n")

for root, _, files in os.walk(base_path):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=path)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            print(f"{path}:  🟢 function → {node.name}")
                        elif isinstance(node, ast.ClassDef):
                            print(f"{path}:  🔵 class   → {node.name}")
            except Exception as e:
                print(f"⚠️ Skipped {path} (error: {e})")
