#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request. You have to use curl
curl -d @$2 $1
