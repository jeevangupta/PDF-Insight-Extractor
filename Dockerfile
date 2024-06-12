
# Define the base image
FROM python:3.10.1-slim

# Set the working directory within the container
WORKDIR /app

# Copy your project code into the container
COPY requirements.txt .

# Install dependencies (if needed)
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501

# Start the application
CMD ["streamlit", "run", "blog_post_insight_extractor.py"]
