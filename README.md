# PWManager

Home made password manager fresh out of the oven
The UI look is generated with PyQt Designer, and the source code and basic toggle animations are from https://github.com/Wanderson-Magalhaes/Toggle_Burguer_Menu_Python_PySide2.
This password manager uses redis as a database to keep your passwords safe, and has a client side encryption/decryption.

# Instructions for running it on windows
There are multiple ways to do it, the first and most forward solution is for you to build it yourself on your machine via pyinstaller or auto-py-to-exe. There is a great tutorial for the auto-py-to-exe: https://www.youtube.com/watch?v=04AAjFBG-bQ
If you install it via pyinstaller or autopy and choose the multiple file solution, it will gather and install the requirements for you. But if you download the released version, which is right now a single file solution, you can simply just download it and copy the platforms directory to the same location where the executable is. The platforms directory can be found in the .zip file included in the released version.

For it to work you will need to install redis on your computer. Right now I only have one work around to do it on windows, with the help of WSL2. 
First step: 
  - https://docs.microsoft.com/en-us/windows/wsl/install-win10
  
Second step:
  - if everything is working and you have a linux distribution running on your windows, eg.: ubuntu, you need to install redis on it with the following command:
    sudo apt-get install redis-server
    
Third step:
 - if the redis-server is installed, you need to change the config file which is usually located in /etc/redis/redis.conf path. Edit requirepass foobar to for example: requirepass pw1
 and then save the changes and restart the redis-server, like sudo service redis-server restart. 
 
 After this you got your redis server up and running, and you can connect to it with the application on the first page. In this example the masterpassword will be pw1.
 If you dont automate the startup of the redis-server, you neeed to start it manually everytime. 
 
 How to automate?
 Since there is no systemd on wsl2 you need a workaround.
 One example is to edit the .bashrc file and add: sudo service redis-server to it. This will ask for your sudo password each time you start up the wsl app. But it wont start right away after windows boot. To do it you can create a .bat file with a simple command like: wsl. After creating the file you can add it to the shell:startup file and reboot your computer and you are good to go!
 
An other solution might be to try out the redis windows version which is not the official release, as redis has no windows support.

# Instructions for running it on Linux
Simply download the Password manager for linux version which is a binary file essentially.

# How it looks

