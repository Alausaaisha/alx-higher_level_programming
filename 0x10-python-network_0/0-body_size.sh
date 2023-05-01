#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI http://1a81dc158b3d.9657af53.alx-cod.online:5000/ | grep -i Content-Length | awk '{print $2}'
