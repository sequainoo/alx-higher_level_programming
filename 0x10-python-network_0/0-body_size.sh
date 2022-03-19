#!/bin/bash
# sends a request to the url argument and returns the content-length in bytes

curl -s --head "$1" | grep 'Content-Length:' | cut -d ' ' -f2
