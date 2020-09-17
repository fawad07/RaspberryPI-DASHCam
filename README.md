# RaspberryPI-DASHCam
Dash board Camera for a car made using a raspberryPi-4 model B
RaspberryPi 3.5 inch Touch screen used for viewing the GUI of the dashCam
RaspberryPi camera Module used to record video
Gui(Tkinter module) implemented using python programming
bash script used to start the application on start up of the raspberryPi

#BEFORE YOU START - UPDATE & UPGRADE RaspberryPi
```yml
sudo apt-get update
sudo apt-get dist-upgrade
```yml

#PART-1
```yml
1. python3 -m venv env
2. source env/bin/activate <-- enter in python enviroment
3. deactivate <-- moved out of python enviroment

# How to start dashcam on startup

```yml
sudo cp dashcam.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dashcam.service
sudo systemctl start dashcam.service
```
# How to Enable Camera Interface
```yml
sudo raspi-config
```
# Test Camera
```yml
raspistill -o l
```

