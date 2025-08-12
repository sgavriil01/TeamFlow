# TeamFlow - AI Project Management Assistant

An AI-powered project management assistant that integrates with GitHub, Jira, and Slack to provide intelligent insights about development workflows.

## 🔒 Security First

This project implements comprehensive security measures:
- **Automated Security Scanning**: GitHub Actions with Bandit and Safety
- **Pre-commit Hooks**: Prevent commits with security issues
- **Environment Protection**: All sensitive data properly secured
- **Dependency Monitoring**: Regular vulnerability checks

## Features

- **Multi-platform Integration**: Connect GitHub repositories, Jira projects, and Slack workspaces
- **AI-Powered Analysis**: RAG-based querying with graceful fallback to rules-based logic
- **Real-time Insights**: Identify blockers, overloaded team members, and project risks
- **Automated Summaries**: Daily/weekly team status reports
- **Multi-tenant Architecture**: Support for multiple organizations

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy + Alembic
- **Database**: PostgreSQL with pgvector for embeddings
- **AI**: OpenAI GPT models with local LLM fallback (Ollama)
- **Integrations**: GitHub OAuth, Jira Cloud API, Slack Bot Framework
- **Testing**: pytest + VCR.py for API mocking
- **Code Quality**: ruff + mypy

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 16+ with pgvector extension
- Poetry for dependency management

### Secure Setup

Use our automated setup script for a secure development environment:

```bash
git clone https://github.com/sgavriil01/TeamFlow.git
cd TeamFlow
poetry install
./setup-dev.sh
```

This script will:
- Create a secure `.env` file from the template
- Install pre-commit security hooks
- Run security scans (Bandit & Safety)
- Verify code quality and tests

### Manual Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Set up the database:
   ```bash
   poetry run alembic upgrade head
   ```

5. Run the development server:
   ```bash
   poetry run uvicorn teamflow.main:app --reload
   ```

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Quality
```bash
poetry run ruff check .
poetry run mypy .
```

### Security Checks
```bash
poetry run bandit -r teamflow/
poetry run safety check
```

### Database Migrations
```bash
poetry run alembic revision --autogenerate -m "Description"
poetry run alembic upgrade head
```

## 🛡️ Security

This project follows security best practices:

- **Environment Variables**: All secrets stored in `.env` (never committed)
- **Automated Scanning**: GitHub Actions run security checks on every commit
- **Pre-commit Hooks**: Prevent insecure code from being committed
- **Dependency Monitoring**: Regular checks for known vulnerabilities
- **Secret Detection**: Prevents accidental credential commits

See [`SECURITY.md`](SECURITY.md) for detailed security policies and procedures.

## Project Structure

```
teamflow/
├── teamflow/           # Main application package
│   ├── api/           # FastAPI routes and endpoints
│   ├── core/          # Core business logic and services
│   ├── db/            # Database models and utilities
│   ├── integrations/  # External API integrations (GitHub, Jira, Slack)
│   └── ai/            # AI/LLM related functionality
├── tests/             # Test suite
├── alembic/           # Database migrations
└── docs/              # Documentation
```

## License

MIT License - see LICENSE file for details.
