#!/bin/bash
# sends a post request to server and returns response body
curl -s --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
