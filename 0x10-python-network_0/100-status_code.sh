#!/bin/bash
# send a request and show status code only
curl -s -o /dev/null -I --w "%{http_code}" "$1"
