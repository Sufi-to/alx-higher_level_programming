#!/bin/bash
# script that sends a post request and display the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
