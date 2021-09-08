#### Stop database
srvctl stop database -d <db>
#### enter as sysdba
sqlplus / as sysdba
startup mount;
alter database archivelog;
#### to disable:
#### alter database noarchivelog

shutdown immediate; (wait)

#get out of sqlplus
#start database
srvctl start database -d <db>