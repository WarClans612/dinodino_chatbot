sudo docker rm $(docker stop $(docker ps -a -q --filter="name=chatbot"))
sudo docker run -d -v /home/nctuca/dinodino_chatbot/chatbot:/var/www/chatbot -p 5000:5000 -p 1112:1112 --net=host --name chatbot chatbot:latest