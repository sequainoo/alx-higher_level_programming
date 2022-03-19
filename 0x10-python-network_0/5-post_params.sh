#!/bin/bash
# sends a post request to server and returns response body
curl --data-urlencode "email=test@gmail.com&subject=I will always be here for PLD" "$1"
