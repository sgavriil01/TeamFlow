# TeamFlow - AI Project Management Assistant

An AI-powered project management assistant that integrates with GitHub, Jira, and Slack to provide intelligent insights about development workflows.

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

### Installation

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

### Database Migrations
```bash
poetry run alembic revision --autogenerate -m "Description"
poetry run alembic upgrade head
```

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
