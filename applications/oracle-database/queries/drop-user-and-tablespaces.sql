-- After dropping the user, you need to, for each related tablespace, take it offline and drop it. 
-- For example if you had a user named 'SAMPLE' and two tablespaces called 'SAMPLE' and 'SAMPLE_INDEX', then you'd need to do the following:

DROP USER SAMPLE CASCADE;
ALTER TABLESPACE SAMPLE OFFLINE;
DROP TABLESPACE SAMPLE INCLUDING CONTENTS;
ALTER TABLESPACE SAMPLE_INDEX OFFLINE;
DROP TABLESPACE SAMPLE_INDEX INCLUDING CONTENTS; 