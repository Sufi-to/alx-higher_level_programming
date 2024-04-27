#!/bin/bash
# script that takes all HTTP methods the server will accept
response=$(curl -s -X OPTIONS -i "$1")
allow_opts=$(echo "$response" | grep -i "Allow")
if [ -n "$allow_opts" ];
then
	methods=$(echo "$allow_opts" | awk '{print substr($0, 8)}')
	echo "$methods"
fi
