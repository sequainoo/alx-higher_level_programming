#!/bin/bash
# sends a request to the url passed with a custom header, displays response body
curl -s --header "X-School-User-Id: 98" "$1"
