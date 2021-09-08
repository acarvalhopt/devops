-- Check invalid objects
select unique owner, OBJECT_NAME, OBJECT_TYPE,OWNER from DBA_OBJECTS where STATUS='INVALID'; 