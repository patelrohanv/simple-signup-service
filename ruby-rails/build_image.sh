#!/bin/bash

# Define the image name
image_name="rails-signup"

# Define the Dockerfile location
dockerfile_location="."

# Build the Docker image
docker build -t $image_name -f Dockerfile $dockerfile_location
