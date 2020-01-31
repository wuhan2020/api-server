# Align with the CI/CD YML
# We cannot use alpine since
# we need to call bash in entrypoint
FROM python:3.6

# Setup workdir
WORKDIR /api-server

# Copy src files
COPY . .

# Install deps
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 9000

# Start the server
ENTRYPOINT [ "bash", "bootstrap"]
