"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os
from pathlib import Path

# Import routers (we'll create these later)
# from teamflow.api.v1 import health, github, jira, slack

# Create FastAPI app
app = FastAPI(
    title="TeamFlow",
    description="AI-powered project management assistant",
    version="0.1.0",
    docs_url="/docs" if os.getenv("DEBUG", "False").lower() == "true" else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up templates
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Root endpoint with basic info."""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "TeamFlow - AI Project Management Assistant"}
    )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "0.1.0",
        "service": "teamflow"
    }


# Include API routers (we'll uncomment these as we create them)
# app.include_router(health.router, prefix="/api/v1", tags=["health"])
# app.include_router(github.router, prefix="/api/v1", tags=["github"])
# app.include_router(jira.router, prefix="/api/v1", tags=["jira"])
# app.include_router(slack.router, prefix="/api/v1", tags=["slack"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "teamflow.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
