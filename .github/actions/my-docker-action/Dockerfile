FROM ubuntu:22.04

# Install dependencies (example)
RUN apt-get update && apt-get install -y \
    bash curl jq && \
    apt-get clean

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
