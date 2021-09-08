#Find and replace in folder all strings with "oldString" by "newString": 
find /tmp/xpto/ -type f -print0 | xargs -0 sed -i 's/oldString/newString/g'

#Find in a certain file a string  "oldString" and replace by "newString":
sed -i 's/oldString/newString/g' /tmp/xpto/example.json