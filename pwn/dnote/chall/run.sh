#!/bin/sh

while :; do
    socat -dd -T60 tcp-l:9999,reuseaddr,fork,keepalive,su=nobody exec:/chall/dnote,stderr
done