#!/bin/bash
# Bash script to sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"
