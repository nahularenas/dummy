import os
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Dummy API", description="Dummy API", version=__version__)

# Log environment variable on startup
env_var = os.getenv("STARTUP_ENV", "development")
logger.info(f"Starting application with environment: {env_var}")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials="*",
    allow_methods="*",
    allow_headers="*",
)


@app.get("/")
async def root():
    """Root endpoint for the API."""
    return {"message": "Welcome to Dummy API", "version": __version__}


if __name__ == "__main__":
    env_var = os.getenv("STARTUP_ENV", "development")
    print(f"Starting application with environment: {env_var}")
    uvicorn.run("main:app", host="0.0.0.0", port=3003, reload=True)
