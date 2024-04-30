#!/bin/bash
# script that sends a request and diplay only status code
curl -so /dev/null -w "%{http_code}" "$1"
