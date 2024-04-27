#!/bin/bash
# script that takes all HTTP methods the server will accept
curl -I -X HEAD "$1" | grep -i allow | sed 's/Allow: //'
