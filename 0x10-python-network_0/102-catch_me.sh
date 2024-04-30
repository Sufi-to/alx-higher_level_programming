#!/bin/bash
# script that makes a request to a given url and
# causes the server to response "you got me"
curl -s -X PUT -H "Orgin:School" -d "user_id=98" 0.0.0.0:5000/catch_me
