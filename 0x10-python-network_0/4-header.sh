#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98
curl -X GET $1 -sH "X-School-User-Id: 98"
