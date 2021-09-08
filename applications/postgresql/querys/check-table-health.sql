-- If the n_dead_tup is big you should think in a Vaccum Clean.
SELECT n_live_tup, n_dead_tup from pg_stat_user_tables where relname = '<yourTable>';