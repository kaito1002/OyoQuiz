PROJECT="OyoQuiz"
OS=$(uname)

cd /home/ubuntu/${PROJECT}

chmod a+x products/deploy.sh
\cp -f products/deploy.sh ../

cd docker
sudo docker-compose down

if [ ${OS} = "Linux" ]; then
  git fetch && git reset --hard origin/master
  sed -i -e "s/#//g" docker-compose.yml
fi

sudo docker-compose build
sudo docker-compose up -d
