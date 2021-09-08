-- List user privileges
select * from dba_role_privs connect by prior granted_role = grantee start with grantee = '&USER' order by 1,2,3;
select * from dba_sys_privs  where grantee = '&USER' or grantee in (select granted_role from dba_role_privs connect by prior granted_role = grantee start with grantee = '&USER') order by 1,2,3;
select * from dba_tab_privs  where grantee = '&USER' or grantee in (select granted_role from dba_role_privs connect by prior granted_role = grantee start with grantee = '&USER') order by 1,2,3,4; 