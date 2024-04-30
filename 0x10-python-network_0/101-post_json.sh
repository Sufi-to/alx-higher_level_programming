#!/bin/bash
# script that sends json Post request and display body response
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
