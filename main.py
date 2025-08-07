import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__

app = FastAPI(title="Dummy API", description="Dummy API", version=__version__)

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
    uvicorn.run("main:app", host="0.0.0.0", port=3003, reload=True)
