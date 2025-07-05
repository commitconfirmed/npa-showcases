FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install python, git and SSH server
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    vim \
    openssh-server \
    git \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Configure an admin user with sudo access
RUN groupadd -r admin && \ 
    useradd -rm -d /app -s /bin/bash -g admin -G sudo admin && \
    echo 'admin:admin' | chpasswd 

RUN mkdir /var/run/sshd && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile

USER admin

WORKDIR /app
COPY --chown=admin:admin app /app

# Install Capirca (break system packages required for codespaces)
ENV PIP_BREAK_SYSTEM_PACKAGES=1
RUN git clone https://github.com/google/capirca.git && \
    cd capirca && \
    python3 setup.py install --user

# Typing-extensions is required for Capirca but not installed by setup.py?
RUN pip3 install --upgrade \
    typing-extensions
    
EXPOSE 22

USER root

ENTRYPOINT ["/usr/sbin/sshd", "-D"]