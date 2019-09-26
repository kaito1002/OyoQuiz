PROJECT="OyoQuiz"
OS=$(uname)

cd /home/ubuntu/${PROJECT}
sudo docker-compose down

if [ ${OS} = "Linux" ]; then
  git fetch && git reset --hard origin/master
  sed -i -e "s/#//g" docker/docker-compose.yml
fi

cd docker
sudo docker-compose build
sudo docker-compose up -d
