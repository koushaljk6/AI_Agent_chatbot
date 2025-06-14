# Use an official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies first for efficient caching
COPY requirements.txt .

# Install dependencies without caching (to keep the image lightweight)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the required ports for FastAPI and Streamlit
EXPOSE 9999 8501

# Set environment variables (optional)
ENV FASTAPI_PORT=9999
ENV STREAMLIT_PORT=8501

# Command to run both FastAPI and Streamlit
CMD ["bash", "-c", "uvicorn backend:app --host 0.0.0.0 --port $FASTAPI_PORT & streamlit run frontend.py --server.port $STREAMLIT_PORT"]