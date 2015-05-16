# The command used to lock the screen
lock_command = "lock"

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

reboot_command = "systemctl reboot"
shutdown_command = "systemctl poweroff"
