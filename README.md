WiFi Spy Tank Remote
====================

A Python application to controll a [WiFi Spy Tank](https://www.kogan.com/au/buy/remote-control-spy-tank-ipad-iphone/) from your desktop!
The tank is also called "Instant Spy Tank".

You can buy one here: [https://www.kogan.com/au/buy/remote-control-spy-tank-ipad-iphone/](https://www.kogan.com/au/buy/remote-control-spy-tank-ipad-iphone/).

![Connected Screenshot](screenshot_video.png)

Installation
------------

- Python3

For ubuntu:
```bash
sudo apt install python3-gi
git clone https://github.com/hmallen/TankRemote
cd TankRemote
virtualenv --python=python3 --system-site-packages env
source env/bin/activate
pip install .

tank_remote
```

- Python2

For ubuntu:
```bash
sudo apt-get install python-gtk2
mkvirtualenv tank --system-site-packages
git clone https://github.com/mic159/TankRemote
cd TankRemote
pip install .

tank_remote
```
