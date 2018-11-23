#
# Python3/bottle web server Dockerfile
#
# This image demonstrates how to set up a Python3/bottle web application using
# the base image pablosan/bottle-py3 as a starting point.
#
# https://github.com/Pablosan/hello-bottlepy
#

# Pull base image
FROM pablosan/bottle-py3

# Install the app
ADD server.py /opt/server/

# Install python packages
RUN pip3 install bottle 

# Expose ports
EXPOSE 80

# Define default command
ENTRYPOINT ["/usr/bin/python3", "/opt/server/server.py"]
