FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install SSH, BIRD and basic network verification tools
RUN apt-get update -y && apt-get install -y \
iproute2 \
bird2 \
tcpdump \
iputils-ping \
sudo \
vim \
openssh-server \
&& apt-get autoremove -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*

# Configure an admin user with sudo access
RUN groupadd -r admin && \ 
useradd -rm -d /app -s /bin/bash -g admin -G sudo admin && \
echo 'admin:admin' | chpasswd 

# Configure SSH server
RUN mkdir /var/run/sshd && \
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22

USER root

# For some reason this directory and file aren't created on bird install which
# will prevent bird from starting
# bird: Cannot create control socket /run/bird/bird.ctl: No such file or directory
RUN mkdir /run/bird
RUN touch /run/bird/bird.ctl

# We will use ansible to configure and then run BIRD depending on the lab topology
ENTRYPOINT ["/usr/sbin/sshd", "-D"]