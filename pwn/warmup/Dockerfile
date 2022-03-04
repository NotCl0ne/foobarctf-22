FROM ubuntu:20.04
RUN apt-get update -y && apt-get install -y \
    lib32z1 xinetd \
 && rm -rf /var/lib/apt/lists/*
RUN useradd error
RUN mkdir /pwn
RUN echo "You've been blocked by our xinetd - try again, and report if this repeats." > /etc/banner_fail
COPY ./ctf.xinetd /etc/xinetd.d/pwn
COPY ./start.sh /start.sh
COPY ./setup.sh /setup.sh
COPY /bin/flag.txt /pwn/flag.txt
COPY /bin/chall /pwn/chall
RUN chown -R root:error /pwn && chmod -R 750 /pwn
RUN chmod +x /setup.sh
RUN chown root:error /start.sh && chmod 750 /start.sh

CMD ["/setup.sh"]

EXPOSE 9999
