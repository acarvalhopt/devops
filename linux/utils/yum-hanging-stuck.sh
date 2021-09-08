rm /var/lib/rpm/__db*
rm /var/lib/rpm/.dbenv.lock
rm /var/lib/rpm/.rpm.lock
yum clean all
rm -f /var/lib/rpm/__db*
rpm --rebuilddb
yum --help