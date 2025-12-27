# Multi Docker

A simple implementation of using multiple Docker containers to run a FastAPI application. The app exposes a basic LLM flow where user queries and answers are stored in MongoDB. The stack separates default Docker services (Ollama and MongoDB) from the custom application container. Llama 3 is used for the LLM portion.

## Stack
- FastAPI app (custom Dockerfile)
- Ollama (LLM runtime with Llama 3)
- MongoDB (stores queries and answers)
- docker-compose to orchestrate services

## How it works
1. FastAPI receives a prompt, calls the Llama 3 model via Ollama, and returns a response.
2. The request and generated answer are persisted in MongoDB.
3. docker-compose brings up the custom app container alongside Ollama and MongoDB as separate services.

## Quick start
1. Ensure Docker and docker-compose are installed.
2. From the repository root run:
   - `docker compose up --build`
3. Access the API at `http://localhost:8000` (adjust if ports change).

## Development notes
- Application code lives in `app/` with its own Dockerfile.
- Ollama and MongoDB run as standard images defined in `docker-compose.yml`.
- Update the compose file to adjust resource limits, ports, or volumes as needed.
