-- check database ASM space
Select name, free_mb, total_mb, round(free_mb/total_mb*100,2) as percentage from v$asm_diskgroup; 