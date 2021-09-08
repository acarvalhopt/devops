# Updating kernel to the latest version
# Command to update
yum update kernel* -y

#Change default kernel
#The following command will print a list of the menu entries present in GRUB2’s configuration.
awk -F\' /^menuentry/{print\$2} /etc/grub2.cfg

# To specify which kernel should be loaded first, pass its number to the grub2-set-default command. 
# The IDs are assigned in order the menu entries appear in the /etc/grub2.cfg file starting with 0.
grub2-set-default X

# Verify the new default kernel
cat /boot/grub2/grubenv |grep saved

# Rebuild GRUB2
grub2-mkconfig -o /boot/grub2/grub.cfg

# Reboot the OS

