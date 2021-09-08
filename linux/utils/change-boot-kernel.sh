#Get available kernel version from /boot/grub2/grub.cfg in section menuentry 
vi /boot/grub2/grubenv 
#Add or replace the entry "saved_entry"

#Example
saved_entry=Oracle VM server, with Xen 4.4.4OVM and Linux 4.1.12-94.6.4.el6uek.x86_64
reboot