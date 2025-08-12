#!/bin/bash

# TeamFlow Development Setup Script

set -e

echo "🔧 Setting up TeamFlow development environment..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📋 Creating .env file from example..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your actual API keys and configuration"
    echo "⚠️  Never commit the .env file to git!"
fi

# Install pre-commit hooks
echo "🔒 Installing pre-commit hooks..."
poetry run pre-commit install

# Run security checks
echo "🛡️  Running security checks..."
poetry run bandit -r teamflow/ -f txt || echo "⚠️  Bandit found some security issues to review"
poetry run safety check || echo "⚠️  Safety found some vulnerability issues to review"

# Run tests
echo "🧪 Running tests..."
poetry run pytest

# Check code quality
echo "📏 Checking code quality..."
poetry run ruff check teamflow/
poetry run mypy teamflow/

echo "✅ Development environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your actual API keys"
echo "2. Set up your database"
echo "3. Run: poetry run python -m teamflow.main"
echo ""
echo "Security reminders:"
echo "- Never commit .env files"
echo "- Use strong, unique secret keys"
echo "- Regularly update dependencies"
echo "- Review security scan results"
