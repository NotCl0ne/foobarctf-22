FROM ubuntu:20.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN mkdir /pirate

RUN mkdir /user
RUN useradd -M -d /user user

RUN echo 'user:tux123' | chpasswd

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/' /etc/ssh/sshd_config

RUN chmod go-rx /usr/bin/passwd

RUN chown -R root:user /user

RUN chmod -R 750 /user

RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN mv /bin/kill /pirate/pkill
RUN mv /bin/ps /pirate/pps
RUN mv /usr/bin/top /pirate/ptop
RUN mv /usr/bin/pkill /pirate/ppkill
RUN mv /usr/bin/pgrep /pirate/ppgrep

RUN chmod -R o-rwx /pirate/

RUN apt-get install -y ncat

EXPOSE 22
EXPOSE 1500
COPY . .
ENTRYPOINT [ "bash","./entrypoint.sh" ]
