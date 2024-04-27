#!/bin/bash
# script that takes all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1"
