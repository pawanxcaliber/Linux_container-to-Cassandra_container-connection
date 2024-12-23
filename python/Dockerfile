FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y python3-pip cron python3-cassandra 

# Copy Python script
COPY test.py /app/test.py

# Configure cron job
RUN crontab -l | { cat; echo "*/5 * * * * python3 /app/test.py"; } | crontab -

# Start cron service
CMD ["cron", "-f"]
