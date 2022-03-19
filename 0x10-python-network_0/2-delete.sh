#!/bin/bash
# makes a delete request to the url and returns body of response ./2-delete.sh url
curl -s -X DELETE "$1"
