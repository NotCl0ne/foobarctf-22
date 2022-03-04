FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
    xinetd \
 && rm -rf /var/lib/apt/lists/*

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY server.py start.sh var root opt lib home dev boot bin ./
COPY etc/flag.txt ./etc/flag.txt

RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

EXPOSE 9999

CMD ["/bin/bash", "start.sh"]
