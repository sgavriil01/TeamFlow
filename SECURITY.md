# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability within TeamFlow, please send an email to [your-email@domain.com]. All security vulnerabilities will be promptly addressed.

## Environment Variables

This project uses environment variables for configuration. **Never commit sensitive information to the repository.**

### Required Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Application secret key (minimum 32 characters)
- `OPENAI_API_KEY`: OpenAI API key for AI features

### Optional Environment Variables

- `GITHUB_CLIENT_ID` & `GITHUB_CLIENT_SECRET`: For GitHub integration
- `JIRA_CLIENT_ID` & `JIRA_CLIENT_SECRET`: For Jira integration
- `SLACK_BOT_TOKEN` & `SLACK_SIGNING_SECRET`: For Slack integration
- `REDIS_URL`: For caching and rate limiting

## Development Setup

1. Copy `.env.example` to `.env`
2. Fill in your actual values in `.env`
3. Never commit the `.env` file

## Production Deployment

- Use environment variables or secure secret management
- Set `DEBUG=False` in production
- Use strong, unique secret keys
- Enable HTTPS
- Regularly rotate API keys and secrets

## Dependencies

- Keep dependencies updated
- Run `poetry audit` to check for known vulnerabilities
- Review dependency changes in pull requests
