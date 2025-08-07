# Dummy API

Dummy API for testing purposes

## Prerequisites

- Python 3.11 or higher
- [UV](https://github.com/astral-sh/uv) package manager

## Setup and Installation

This project uses UV for dependency management and a Makefile for common tasks.

### Initialize the Project

To set up the virtual environment and install all dependencies:

```bash
make init
```

This command will:
- Create a virtual environment using Python 3.12
- Install all project dependencies

## Running the Application

To start the Dummy API:

```bash
make start
```

The API will be available at http://localhost:3003 with automatic reload enabled for development.

## Available Make Commands

| Command | Description |
|---------|-------------|
| `make help` | Display help information |
| `make init` | Initialize the project |
| `make start` | Start the API server |
