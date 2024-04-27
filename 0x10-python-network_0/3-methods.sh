#!/bin/bash
# script that takes all HTTP methods the server will accept
curl -SI "$1" | grep -i allow | sed -ne 's/^Allow: //p'
