# When building with Docker Desktop on a Mac with Apple silicon, but
# destined for k8s, the platform needs to be specified ...
FROM --platform=linux/amd64 faucet/python3

WORKDIR /helloworld

COPY *.sh ./
COPY helloworld ./
RUN ./build.sh

EXPOSE 5000

CMD ["/bin/sh", "start.sh"]
