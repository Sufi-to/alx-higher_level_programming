#!/bin/bash
# script that takes a url and displays the size of body
curl -I -s "$1" | awk '/Content-Length/ {print $2}'
