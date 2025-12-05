FROM python:3.11-slim

# Install boto3
RUN pip install boto3

# Copy script
COPY entrypoint.py /entrypoint.py

# Set entrypoint
ENTRYPOINT ["python", "/entrypoint.py"]