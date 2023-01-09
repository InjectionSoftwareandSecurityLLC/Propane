FROM ubuntu:latest
RUN apt update -y && apt install python3 apache2 -y
WORKDIR Propane/
COPY . .
RUN bash setup.sh
CMD service apache2 start && service apache2 status && cd /var/www/ && sed -i "s|isDocker = False|isDocker = True|" propane.py && python3 propane.py