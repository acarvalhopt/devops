# Error "Too many open files" we should change the limit in the correspondent service.
vim /usr/lib/systemd/system/example.service
#add in the end of the file:
LimitNOFILE=65536