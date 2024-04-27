#!/bin/bash
# script that sends a get request and display the body
# if the status code is 200
curl -s -X GET -L "$1"
