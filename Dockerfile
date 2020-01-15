FROM ubuntu:bionic
RUN apt-get update
RUN apt-get -y install lighttpd aurora
COPY aurora.cgi /usr/www/cgi-bin/
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
CMD lighttpd -Df /etc/lighttpd/lighttpd.conf
