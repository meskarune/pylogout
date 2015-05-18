# The command used to lock the screen
lock_command = "lock"

# The command used to close all open windows gracefully
# default reqires that wmctrl be installed
close_command = "wmctrl -l -p | awk '{print $3}' | while read PID; do kill -15
$PID; done"

# The command used to logout from the current session
# i3
# logout_command = "i3-msg exit"
# herbstluftwm
logout_command = "herbstclient quit"

# Suspend and Hibernate

# Systemd
#suspend_command = "systemctl suspend"
#hibernate_command = "systemctl hibernate"

# Pm-utils
suspend_command = "pm-suspend"
hibernate_command = "pm-hibernate"

# The command run to reboot the computer
reboot_command = "systemctl reboot"

# The command run to turn off the computer
shutdown_command = "systemctl poweroff"
