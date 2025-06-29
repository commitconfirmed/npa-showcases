FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install SSH and basic networking tools
RUN apt-get update -y && apt-get install -y \
iproute2 \
tcpdump \
iputils-ping \
openssh-server \
sudo \
vim \
gcc \
make \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*

# Manual install of iperf3 to use latest version as ubuntu apt only has 3.16
ENV IPERF_VERSION=3.19
RUN wget https://downloads.es.net/pub/iperf/iperf-${IPERF_VERSION}.tar.gz
RUN tar -xzf iperf-${IPERF_VERSION}.tar.gz && \
cd iperf-${IPERF_VERSION} && \
./configure && \
make && \
make install
RUN ldconfig -v

# Configure an admin user with sudo access
RUN groupadd -r admin && \ 
useradd -rm -d /app -s /bin/bash -g admin -G sudo admin && \
echo 'admin:admin' | chpasswd 

RUN mkdir /var/run/sshd && \
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22

USER root

ENTRYPOINT ["/usr/sbin/sshd", "-D"]