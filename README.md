
## Install deb By Tkinter:
You can install any deb file just by clicking on it
## Get Started
Save the following Python script as installdeb.py in your desired directory, for example, /home/your_username/installdeb.py.
    

## Screenshot:
![pic1](https://i.ibb.co/0YtCvqT/photo-2024-07-18-02-15-09.jpg)


<br /><br />

## Create file 
```bash
nano ~/.local/share/applications/open_deb.desktop
```
## Write thi in open_deb.desktop
```bash

[Desktop Entry]
Name=Lkt install
Exec=python3 /home/your_username/installdeb.py %f
Type=Application
MimeType=application/vnd.debian.binary-package
```
## and add this code in termnual
```bash
xdg-mime default open_deb.desktop application/vnd.debian.binary-package
```
