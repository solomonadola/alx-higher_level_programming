#!/bin/bash
# Get the byte size of the HTTP response header of  a given URL.

curl -s "$1" | wc -c
