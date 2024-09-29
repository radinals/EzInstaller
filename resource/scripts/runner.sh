#!/usr/bin/env bash

count=1
total_scripts="$#"

printf "\n[%s]\n\n" "Starting Installation Process, do not close this window."

while [ $# -gt 0 ]; do
    if [ -x "$1" ]; then
        printf "%s\n" "# Executing Installer Script '$(basename $1)' ($count/$total_scripts) #"
        bash -e "$1"
        count=$((count + 1))
    fi
    shift
done

printf "\n[%s]\n" "Starting Installation Completed, you can now safely close this window."

