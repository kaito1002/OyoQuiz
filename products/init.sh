PROJECT="OyoQuiz"
REPO="https://github.com/kaito1002/OyoQuiz.git"

# docker setup
cd /home/ubuntu
sudo apt-get -y update && sudo apt-get -y upgrade
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get -y remove docker-ce && sudo apt-get install -y docker-ce=18.06.1~ce~3-0~ubuntu

# webhook setup
cp ${PROJECT}/products/webhook.py ./
cp ${PROJECT}/products/webhook.service ./
cp ${PROJECT}/products/deploy.sh ./

printf "Input Webhook Key >> "; read KEY
sed -i -e "s/Input Key In Product/"${KEY}"/g" webhook.py
rm webhook.py-e
sudo cp webhook.service /etc/systemd/system/

sudo chmod 0755 ./webhook.py
sudo systemctl enable webhook.service
sudo systemctl start webhook.service

# deploy application
chmod a+x deploy.sh && ./deploy.sh
