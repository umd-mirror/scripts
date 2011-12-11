#!/bin/bash

if [ $# = 1 ]; then
  pkg=$1
else
  echo USAGE: $0 mirror_to_check
  exit -1
fi

if [ -f ~/var/trigger/$pkg ]; then
  rm -f ~/var/trigger/$pkg
  echo "Updating $pkg (triggered)"

  ~/scripts/run_mirror.py $pkg || exit -1
fi

exit 0

