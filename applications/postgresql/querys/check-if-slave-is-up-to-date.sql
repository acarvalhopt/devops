-- from Master:
SELECT pg_current_wal_lsn(); 

-- from Slave
SELECT pg_last_wal_receive_lsn();
SELECT pg_last_wal_replay_lsn(); 

-- The results should be equal in both machines, if not, it's because the slave is not synchronized.