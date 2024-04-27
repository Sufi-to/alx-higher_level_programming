#!/bin/bash
# script that sends a get request and display the body
# if the status code is 200
response=$(curl -s -w "%{http_code}" -L "$1")
stat_code=$(echo "$response" | tail -c 4)
if [ "$stat_code" = "200" ]
then
	echo "$response" | head -c 4
fi
