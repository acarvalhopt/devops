SELECT dbms_metadata.get_ddl('USER', :name)
  FROM dual
UNION ALL
SELECT dbms_metadata.get_granted_ddl('ROLE_GRANT', grantee)
  FROM dba_role_privs
 WHERE grantee = :name
   AND ROWNUM = 1
UNION ALL
SELECT dbms_metadata.get_granted_ddl('DEFAULT_ROLE', grantee)
  FROM dba_role_privs
 WHERE grantee = :name
   AND ROWNUM = 1
UNION ALL
SELECT dbms_metadata.get_granted_ddl('SYSTEM_GRANT', grantee)
  FROM dba_sys_privs          sp,
       system_privilege_map   spm
 WHERE sp.grantee = :name
   AND sp.privilege = spm.name
   AND spm.property <> 1
   AND ROWNUM = 1
UNION ALL
SELECT dbms_metadata.get_granted_ddl('OBJECT_GRANT', grantee)
  FROM dba_tab_privs
 WHERE grantee = :name
   AND ROWNUM = 1
UNION ALL
SELECT dbms_metadata.get_granted_ddl('TABLESPACE_QUOTA', username)
  FROM dba_ts_quotas
 WHERE username = :name
   AND ROWNUM = 1