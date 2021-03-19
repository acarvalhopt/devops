# find all Json files inside a folder and replace the json_field value by a newValue.
# Note: jq needs "--arg VAR" to pass a variable ('VAR' can be the name you want.)

newValue = "helloWord"

find destinationFolder/ -name "*.json" | while read line; do 
	jq --arg VAR "$newValue" '."json_field"=$VAR' $line > temp && mv -f temp $line 
done