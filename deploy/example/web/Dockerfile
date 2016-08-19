FROM redis
RUN apt-get update &&\
    apt-get install -y tcpdump fping iperf netcat net-tools curl
COPY docker-entrypoint.sh /

EXPOSE 6379 5001
ENTRYPOINT ["/docker-entrypoint.sh"]
