#!/bin/bash
# script that takes a url and displays the size of body
curl -w "%{size}\n" -o /me -s "$1"
