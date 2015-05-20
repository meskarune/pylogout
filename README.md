# pylogout

Python cli and gtk system exit applet based off cb\_exit

Running pylogout gives the user the following options:

    Usage: pylogout [OPTIONS]
    
    Leave the current Session
    
     Options:
       --version         show program's version number and exit
       -h, --help        show this help message and exit
       -S, --screenlock  Lock the screen
       -l, --logout      Close open programs and logout
       -s, --suspend     Lock the screen and suspend
       -b, --hibernate   Lock the screen and hibernate
       -r, --reboot      Close open programs and reboot
       -p, --poweroff    Close open programs and poweroff

Commands can be set in the config.py file

To-do:

* icons
* make it prettier
* system tray?
* toggle screen blanking
