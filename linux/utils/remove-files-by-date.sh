# remove all files and preserve last 5 days
find /path/to/files* -mtime +5 -exec rm {} \;