#!/bin/bash
# Bash script to make a request that causes the server to respond with a message containing You got me!
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1" -i
