FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY ctf.xinetd /etc/xinetd.d/ctf

COPY server.py etc/flag.txt /

CMD ["xinetd", "-dontfork"]

EXPOSE 9999
