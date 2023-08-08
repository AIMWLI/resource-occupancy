# Simple Python Dockerized Application

Build the image using the following command

```bash
DOCKER_BUILDKIT=0 docker buildx  build --platform linux/amd64 -t generativepretrainedtransformer:v1 .
```

Run the Docker container using the command shown below.

```bash
docker run -idt -e m=2 -e c=2 generativepretrainedtransformer:v1
```
