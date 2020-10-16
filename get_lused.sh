#!/bin/bash

# Add a sudoers entry to allow the mirror user to call this script
# so it doesn't need permission to run all ZFS commands
# For example, you could do it (with `sudoedit /etc/sudoers.d/mirror`) like this:
# mirror ALL=(root) NOPASSWD: /home/mirror/scripts/get_lused.sh

if [ $# -ne 1 ]; then
    echo USAGE: "$0" /path/to/mountpoint
    exit -1
fi

canonical=$(readlink -f -- "$1")

if [ "$canonical" != "$1" ]; then
    echo ERROR: Argument must be a canonical path.
    exit -1
fi

if ! mountpoint -q -- "$canonical"; then
    echo ERROR: Argument must be a mountpoint.
    exit -1
fi

/sbin/zfs get -H -o value -p logicalused -- "$canonical"
