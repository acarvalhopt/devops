delete FROM alerts where age(to_timestamp(alerts.clock)) > interval '7 days';
delete FROM acknowledges where age(to_timestamp(acknowledges.clock)) > interval '7 days';
delete FROM events where age(to_timestamp(events.clock)) > interval '7 days';
delete FROM history where age(to_timestamp(history.clock)) > interval '7 days';
delete FROM history_uint where age(to_timestamp(history_uint.clock)) > interval '7 days' ;
delete FROM history_str  where age(to_timestamp(history_str.clock)) > interval '7 days' ;
delete FROM history_text where age(to_timestamp(history_text.clock)) > interval '7 days' ;
delete FROM history_log where age(to_timestamp(history_log.clock)) > interval '7 days' ;
delete FROM trends where age(to_timestamp(trends.clock)) > interval '90 days';
delete FROM trends_uint where age(to_timestamp(trends_uint.clock)) > interval '90 days' ;

delete from history where itemid not in (select itemid from items where status='0');
delete from history_uint where itemid not in (select itemid from items where status='0');
delete from history_str where itemid not in (select itemid from items where status='0');
delete from history_text where itemid not in (select itemid from items where status='0');
delete from history_log where itemid not in (select itemid from items where status='0');
delete from trends where itemid not in (select itemid from items where status='0');
delete from trends_uint where itemid not in (select itemid from items where status='0');