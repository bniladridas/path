#!/bin/bash

# Rewrite commit messages to lowercase and truncate first line to 60 chars
git filter-branch --msg-filter '
read -r msg
first_line=$(echo "$msg" | head -n1 | tr "[:upper:]" "[:lower:]" | cut -c1-60)
rest=$(echo "$msg" | tail -n +2)
echo "$first_line"
if [ -n "$rest" ]; then
    echo "$rest"
fi
' -- --all
