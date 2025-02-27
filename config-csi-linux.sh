sudo apt update
sudo apt full-upgrade -y
sudo apt autoremove

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.13
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1
sudo update-alternatives --config python3

