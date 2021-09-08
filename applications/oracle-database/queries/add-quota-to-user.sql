select * from dba_ts_quotas;
-- Check Users with Quotas filled up:
select * from dba_ts_quotas where blocks=max_blocks; 

select tablespace_name, username, bytes, max_bytes
    from dba_ts_quotas
    --where tablespace_name = 'EXAMPLE_TBS' 
    where username = 'EXAMPLE_USER';
    
alter user EXAMPLE_USER quota 40M on EXAMPLE_TBS; 

-- Unlimited Quota
alter user EXAMPLE_USER quota UNLIMITED on EXAMPLE_TBS; 

select * from dba_sys_privs where privilege like 'UNLIMITED%';