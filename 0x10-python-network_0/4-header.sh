#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL
curl -LsX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
