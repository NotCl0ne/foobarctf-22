FROM frolvlad/alpine-glibc:glibc-2.32

RUN apk update && apk add socat

COPY chall /chall
WORKDIR /chall
RUN chmod 644 flag.txt && \
    chmod 500 run.sh

EXPOSE 9999

ENTRYPOINT ["/chall/run.sh"]