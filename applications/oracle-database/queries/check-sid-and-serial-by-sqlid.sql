-- check sid and serial by sqlid
-- Get sqlid from SQL monitor in enterprise manager
SELECT SID, SERIAL#, SQL_ID, osuser, machine
FROM GV$SESSION
WHERE USERNAME IS NOT NULL AND STATUS = 'ACTIVE' AND SQL_ID IS NOT NULL and ownerid = '<sqlid>';