#!/bin/bash

# TeamFlow Development Helper Script

set -e

# Add Poetry to PATH
export PATH="$HOME/.local/bin:$PATH"

case "$1" in
    "install")
        echo "Installing dependencies..."
        poetry install
        ;;
    "run")
        echo "Starting development server..."
        poetry run uvicorn testomax.main:app --reload --host 0.0.0.0 --port 8000
        ;;
    "test")
        echo "Running tests..."
        poetry run pytest tests/ -v
        ;;
    "lint")
        echo "Running linter..."
        poetry run ruff check .
        ;;
    "format")
        echo "Formatting code..."
        poetry run ruff format .
        ;;
    "typecheck")
        echo "Running type checker..."
        poetry run mypy testomax/
        ;;
    "shell")
        echo "Starting Poetry shell..."
        poetry shell
        ;;
    *)
        echo "TeamFlow Development Helper"
        echo ""
        echo "Usage: $0 {install|run|test|lint|format|typecheck|shell}"
        echo ""
        echo "Commands:"
        echo "  install    - Install project dependencies"
        echo "  run        - Start development server"
        echo "  test       - Run test suite"
        echo "  lint       - Run code linter"
        echo "  format     - Format code"
        echo "  typecheck  - Run type checker"
        echo "  shell      - Start Poetry shell"
        exit 1
        ;;
esac
