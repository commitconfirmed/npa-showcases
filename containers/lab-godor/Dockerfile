# A basic Dockerfile for a Go development/execution environment with SSH access
# That we can use in codespaces & containerlab
FROM ubuntu:latest

# Prompt avoidance
ENV DEBIAN_FRONTEND=noninteractive

USER root
WORKDIR /root

# Some standard Ubuntu packages for troubleshooting and a SSH server
RUN apt-get update -y && apt-get install -y \
iproute2 \
tcpdump \
iputils-ping \
vim \
curl \
openssh-server \
sudo \
&& rm -rf /var/lib/apt/lists/*

# Download Go
RUN curl -OL https://golang.org/dl/go1.23.4.linux-amd64.tar.gz

# Install Go
RUN tar -C /usr/local -xzf go1.23.4.linux-amd64.tar.gz
RUN rm go1.23.4.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin

# Download Go packages
#RUN go get -u github.com/golang/dep/cmd/dep
#RUN go get -d github.com/osrg/gobgp || exit 0

# Configure an admin user with sudo access
RUN groupadd -r admin && useradd -rm -d /home/admin -s /bin/bash -g admin -G sudo -u 666 admin && \
echo 'admin:admin' | chpasswd

RUN mkdir /var/run/sshd && \
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile

# Set Go environment variables in the admin user's profile
# This is so that the scripts that containerlab copies to /app
# Can be run 
USER admin
RUN mkdir -p /home/admin/go \
    && echo 'export PATH=$PATH:/usr/local/go/bin' >> /home/admin/.profile \
    && echo 'export GOPATH=/home/admin/go' >> /home/admin/.profile \
    && echo 'export GOCACHE=/home/admin/go/.cache' >> /home/admin/.profile

EXPOSE 22

USER root

ENTRYPOINT ["/usr/sbin/sshd", "-D"]