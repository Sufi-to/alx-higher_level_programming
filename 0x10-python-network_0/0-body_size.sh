#!/bin/bash
# script that takes a url and displays the size of body
curl -w "%{size}\n" -o /dev/null -s "$1"
