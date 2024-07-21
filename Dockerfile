# Use Debian base image
FROM debian:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    cowsay \
    fortune-mod \
    netcat-openbsd \
    bash && \
    apt-get clean

# Add /usr/games to the PATH
ENV PATH="/usr/games:${PATH}"

# Copy script to container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Verify installation of packages
RUN command -v /usr/games/cowsay || echo "cowsay not found" \
    && /usr/games/cowsay "Cowsay is installed" \
    && command -v /usr/games/fortune || echo "fortune not found" \
    && /usr/games/fortune \
    && command -v nc || echo "nc not found"

# Expose port 4499
EXPOSE 4499

# Set the entrypoint to the script (adjust if necessary)
ENTRYPOINT ["/usr/local/bin/wisecow.sh"]

