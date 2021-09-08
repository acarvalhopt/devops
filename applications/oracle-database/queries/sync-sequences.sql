-- Sync sequences
select max(id) from <table>;
--example: 4593

select <sequence>.nextval from dual;
--example: 4022

declare 
v_seq number;
begin
    for i in 1..600 loop
        select <sequence>.nextval into v_seq from dual;
    end loop;
end;