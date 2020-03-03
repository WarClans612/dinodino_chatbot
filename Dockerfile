FROM mongo:4.2

RUN apt-get update -y
RUN apt-get install python3-pip python3-dev nginx vim -y
RUN apt-get clean

ADD chatbot/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ADD nginx_conf /etc/nginx/sites-available/

RUN rm -f /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/nginx_conf /etc/nginx/sites-enabled

ADD start.sh /start.sh

CMD ["sh", "/start.sh"]
