
#Error:
#systemd[1]: httpd.service: main process exited, code=exited, status=1/FAILURE
#kill[5312]: kill: cannot find process ""
#systemd[1]: httpd.service: control process exited, code=exited status=1
#systemd[1]: Failed to start The Apache HTTP Server.

#Shell script to clear up IPC where no processes are attached
for i in `ipcs -s | awk '/apache/ {print $2}'`; do (ipcrm -s $i); done