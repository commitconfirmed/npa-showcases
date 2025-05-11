FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install python and SSH server
RUN apt-get update -y && apt-get install -y \
python3 \
python3-pip \
iputils-ping \
vim \
openssh-server \
&& rm -rf /var/lib/apt/lists/*

# Install nornir
# Note: PIP_BREAK_SYSTEM_PACKAGES is required to get this working
# in github codespaces without doing a venv in a docker container
# (yes i'm lazy and why do I need a venv in a docker image?)
ENV PIP_BREAK_SYSTEM_PACKAGES=1
RUN pip3 install --upgrade \
nornir \
nornir_utils \
nornir_napalm \
nornir_netmiko \
nornir_netbox \
nornir_rich \
nornir_nautobot \
nornir_scrapli \
requests

# Configure an admin user with sudo access
RUN groupadd -r admin && \ 
useradd -rm -d /app -s /bin/bash -g admin -G sudo admin && \
echo 'admin:admin' | chpasswd 

RUN mkdir /var/run/sshd && \
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile

USER admin

# Create empty known_hosts file for SSH key importing by nornir
# I don't believe this is needed? as netmiko does this for us
RUN mkdir ~/.ssh && \
touch ~/.ssh/known_hosts

WORKDIR /app
COPY --chown=admin:admin app /app

EXPOSE 22

USER root

ENTRYPOINT ["/usr/sbin/sshd", "-D"]