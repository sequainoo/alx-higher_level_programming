#!/bin/bash
# requests for request methods/options that are allowed for the server
curl -s -X OPTIONS --head "$1" | grep 'Allow:' | cut -d ' ' -f2-
