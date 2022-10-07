FROM python

WORKDIR /app

COPY . /app

CMD ["python", "rng.py"]

# After we build this image, we need to run it with interactive mode and
# in terminal mode as well. To do this we will use the command:
# docker run -it image_id (-i for interactive mode, -t for terminal)
# Also to start container with interactive mode:
# docker start -ai container_name (-a for attached mode, -i for interactive mode)