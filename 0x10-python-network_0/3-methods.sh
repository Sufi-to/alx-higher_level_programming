#!/bin/bash
# script that takes all HTTP methods the server will accept
curl -sX OPTIONS -I "$1"
