FROM python:3.13.11-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Create current directory and set it as the working directory
WORKDIR /app

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked

WORKDIR /app
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

## RUN pip install pandas pyarrow

COPY main.py pipeline.py ./

ENTRYPOINT ["python", "pipeline.py"]
CMD ["1"]
