FROM ubuntu:latest
RUN apt update -y && apt install python3 apache2 -y
RUN service apache2 start
WORKDIR Propane/
COPY . .
RUN bash setup-headless.sh /var/www/
CMD cd /var/www/ && ls -la && python3 propane.py