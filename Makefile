VENV=.venv

.PHONY: help init start

help:
	@echo "Available commands:"
	@echo "  help: Display this help message"
	@echo "  init: Initialize the virtual environment"
	@echo "  start: Start the application"

init:
	@echo "Initializing project..."
	uv venv --python 3.12
	/bin/bash -c "source .venv/bin/activate && uv sync"

start:
	@echo "Starting Dummy API..."
	/bin/bash -c "source .venv/bin/activate && uv run uvicorn main:app --host 0.0.0.0 --port 3003 --reload"
