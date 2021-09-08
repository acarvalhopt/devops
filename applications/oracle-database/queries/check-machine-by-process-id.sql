select a.spid server, b.process client, b.username, b.machine, b.sid, b.serial#    
from v$process a , v$session b
where (a.addr = b.paddr) and a.spid in ( <pid>);


-- generate kill session script
select a.spid server, b.process client, b.username, b.machine, b.sid, b.serial#, 'alter system kill session ''' || b.sid || ',' || b.serial#||''' IMMEDIATE; '
from v$process a , v$session b
where (a.addr = b.paddr) and a.spid in (<pid>);