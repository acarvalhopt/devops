# Execute this command

ls -ld /proc/*/fd/* 2>&1 | fgrep '(deleted)' 

#If you get any result
find /proc/*/fd -ls 2> /dev/null | awk '/deleted/ {print $11}'| xargs -n 1 truncate -s 0