-- check size of the tables
SELECT owner,
    segment_name,
    segment_type,
    tablespace_name,
    bytes/1048576/1024 GB,
    initial_extent,
    next_extent,
    extents,
    pct_increase
FROM
    DBA_SEGMENTS
WHERE
    --OWNER = 'table owner' AND
    --SEGMENT_NAME = 'table name' AND
    SEGMENT_TYPE = 'TABLE' order by GB desc; 