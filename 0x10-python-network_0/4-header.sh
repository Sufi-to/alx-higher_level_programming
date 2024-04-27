#!/bin/bash
# script that sends a get request to the url and the body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
