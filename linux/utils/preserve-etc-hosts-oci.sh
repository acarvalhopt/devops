#Any changes you make to the /etc/hosts and /etc/resolve.conf files will be overwritten whenever the DHCP lease is renewed or the instance is rebooted. 
# To persist your changes, add the following line to /etc/oci-hostname.conf:

PRESERVE_HOSTINFO=2
#If the /etc/oci-hostname.conf does not exist, create it.