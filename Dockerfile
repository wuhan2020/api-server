# Align with the CI/CD YML
FROM python:2.7

# Setup workdir
WORKDIR /api-server

# Copy src files
COPY . .

# Install deps
RUN pip install -r requirements.txt

# Temporary hack until PR https://github.com/wuhan2020/api-server/pull/27 is merged
RUN mkdir -p /home/wuhan2020/wuhan2020

# Expose port 5000
EXPOSE 5000

# Start the server
ENTRYPOINT [ "bash", "bootstrap"]
