FROM node:16

RUN apt-get update -y &&\
    apt-get install -y lib32z1 xinetd

WORKDIR /home/node

COPY src/ctf.xinetd /etc/xinetd.d/ctf
COPY src/start.sh src/chall.js src/flag.txt ./

RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail
RUN chmod +x start.sh

USER node
CMD ["./start.sh"]

EXPOSE 9999
