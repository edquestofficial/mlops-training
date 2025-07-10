FROM python:3.11-slim

WORKDIR /app

# Install curl and uv
RUN apt-get update && \
    apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | bash && \
    cp /root/.local/bin/uv /usr/local/bin/uv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Verify uv installation
RUN uv --version

# Copy project files
COPY pyproject.toml ./
COPY ice_cream.py ./
COPY ice_cream.csv ./
COPY app.py ./
COPY linear_regression_model.pkl ./

# Create virtual environment and install dependencies into it
RUN uv venv .venv && \
    uv pip install --python=.venv/bin/python .

# Set environment variables for virtual environment usage
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Expose port for FastAPI
EXPOSE 8001

# Run the app with uvicorn from the virtual environment
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]