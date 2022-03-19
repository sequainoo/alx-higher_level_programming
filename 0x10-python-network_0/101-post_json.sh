#!/bin/bash
# sends json file and return response body
curl -s -d @"$2" --header "Content-Type: application/json" "$1"
