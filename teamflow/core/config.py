"""Configuration management for TeamFlow."""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings."""
    
    # Database
    database_url: str = Field(..., description="Database connection URL")
    
    # API Keys
    openai_api_key: Optional[str] = Field(None, description="OpenAI API key")
    github_client_id: Optional[str] = Field(None, description="GitHub OAuth client ID")
    github_client_secret: Optional[str] = Field(None, description="GitHub OAuth client secret")
    jira_client_id: Optional[str] = Field(None, description="Jira OAuth client ID")
    jira_client_secret: Optional[str] = Field(None, description="Jira OAuth client secret")
    slack_bot_token: Optional[str] = Field(None, description="Slack bot token")
    slack_signing_secret: Optional[str] = Field(None, description="Slack signing secret")
    
    # Application
    secret_key: str = Field("dev-secret-key-change-me", description="Secret key for sessions")
    debug: bool = Field(False, description="Debug mode")
    log_level: str = Field("INFO", description="Log level")
    
    # AI Configuration
    ai_model_router: str = Field("gpt-4o-mini", description="AI model for routing")
    ai_model_summarizer: str = Field("gpt-4o", description="AI model for summaries")
    ai_embedding_model: str = Field("text-embedding-3-small", description="AI embedding model")
    ai_max_tokens: int = Field(4000, description="Maximum AI tokens")
    
    # Optional features
    redis_url: Optional[str] = Field(None, description="Redis connection URL")
    ollama_base_url: str = Field("http://localhost:11434", description="Ollama base URL")
    enable_local_llm: bool = Field(False, description="Enable local LLM")
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


# Global settings instance
settings = Settings()
