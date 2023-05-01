#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI https://github.com/ | grep -i Content-Length | awk '{print $2}'
