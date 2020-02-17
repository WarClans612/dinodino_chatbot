cd /var/www/chatbot

gunicorn --workers 3 --bind unix:chatbot.sock --daemon -m 007 --user www-data --worker-class gevent wsgi:app
nginx
tail -F /var/log/nginx/access.log
