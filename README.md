# remove_vbox_log
Simple Python 3 script to remove all VirtualBox log files for current user. Usually they are located at home directory where all VMs are stored. Each VM has own log files, up to three.

# Installation
To execute a script, you need Python 3 installed.
Then clone this repository and go to downloaded directory:

    git clone https://github.com/gangural/remove_vbox_log
    cd remove_vbox_log

That's it!

# Usage
`python3 main.py`

Sample output:

    Removed /home/user/VirtualBox VMs/Windows/Windows 7 64 bit/Logs/VBox.log.2
    Removed /home/user/VirtualBox VMs/Windows/Windows 7 64 bit/Logs/VBox.log
    Removed /home/user/VirtualBox VMs/Windows/Windows 7 64 bit/Logs/VBox.log.1
    Removed /home/user/VirtualBox VMs/Windows/Windows 7 64 bit/Logs/VBox.log.3
    Removed /home/user/VirtualBox VMs/Windows/Windows 10/Logs/VBox.log.2
    Removed /home/user/VirtualBox VMs/Windows/Windows 10/Logs/VBox.log
    Removed /home/user/VirtualBox VMs/Windows/Windows 10/Logs/VBox.log.1
    Removed /home/user/VirtualBox VMs/Windows/Windows 10/Logs/VBox.log.3
