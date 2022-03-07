FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY src/ctf.xinetd /etc/xinetd.d/ctf

COPY src/server.py src/flag.txt /

CMD ["xinetd", "-dontfork"]

EXPOSE 9999
