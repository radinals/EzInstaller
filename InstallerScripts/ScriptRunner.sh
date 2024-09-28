#!/usr/bin/env bash

while [ $# -gt 0 ]; do
    if [ -x "$1" ]; then
        bash -e "$1"
    fi
    shift
done

