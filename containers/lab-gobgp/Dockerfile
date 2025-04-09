FROM ubuntu:latest

# Prompt avoidance
ENV DEBIAN_FRONTEND=noninteractive
ENV GO_VERSION=1.24.2

USER root
WORKDIR /root

# # Some standard Ubuntu packages for network troubleshooting
RUN apt-get update -y && apt-get install -y \
iproute2 \
tcpdump \
iputils-ping \
curl \
&& rm -rf /var/lib/apt/lists/*

# Download & Install Go 
RUN curl -OL https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go.${GO_VERSION}.linux-amd64.tar.gz
RUN rm go${GO_VERSION}.linux-amd64.tar.gz

# Set Go environment variables
ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH /usr/local/go

# Download GoBGP
RUN go get -u github.com/golang/dep/cmd/dep
RUN go get -d github.com/osrg/gobgp || exit 0

# Install GoBGP
RUN \
    cd ${GOPATH}/src/github.com/osrg/gobgp/cmd && \
    go install ./gobgp && \
    go install ./gobgpd

COPY --from=0 /go/bin/gobgp  /usr/local/bin/gobgp
COPY --from=0 /go/bin/gobgpd /usr/local/bin/gobgpd

ENTRYPOINT ["/usr/local/bin/gobgpd", "-f", "gobgpd.conf"]