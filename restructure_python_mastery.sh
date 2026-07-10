#!/bin/bash
# Restructure PYTHON_MASTERY repo: clean junk, fix folder names, scaffold empty placeholders
# Run from repo root: bash restructure_python_mastery.sh
set -e

echo "== Deleting tempCodeRunnerFile.py (all occurrences) =="
find . -name "tempCodeRunnerFile.py" -type f -delete

echo "== Deleting __pycache__ folders (all occurrences) =="
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

echo "== Renaming folders with spaces/special characters to snake_case =="
mv "05_Exercises/Conditionals_&_Loops" "05_Exercises/conditionals_and_loops"
mv "05_Exercises/File Handling & Exceptions" "05_Exercises/file_handling_and_exceptions"
mv "04_Software_Engineering/git (version control)" "04_Software_Engineering/git"

echo "== Adding .gitkeep to empty placeholder folders =="
touch 03_Advanced/.gitkeep
touch 05_Exercises/Lists/.gitkeep
touch 04_Software_Engineering/databases/.gitkeep
touch 04_Software_Engineering/git/.gitkeep
touch 04_Software_Engineering/subprocess/.gitkeep
touch 04_Software_Engineering/testing/.gitkeep
touch 04_Software_Engineering/threading/.gitkeep

echo "== Done. Review with: ls -la and git status (if already a git repo) =="