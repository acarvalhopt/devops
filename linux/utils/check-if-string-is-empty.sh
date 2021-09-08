#Note: You can do with -z option but -z only checks if string is null, 
# if is with spaces it will return that the string has characters, 
# so with the below condition we can remove the spaces and check if the string is really empty.

if $1 = *[!\ ]* && $2 = *[!\ ]*
then
    echo "not empty"
else 
    echo "empty"
fi 