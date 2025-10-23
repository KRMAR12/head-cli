#!/bin/bash


if [ $# -eq 0 ]; then
  echo "Usage: head_cli <file> [options]"
  exit 1
fi


FILE="$1"
shift
OPTIONS="$@"


MSYS_NO_PATHCONV=1 docker run --rm -v "C:/Users/kravc/Desktop/head-cli:/data" head-cli-image /data/"$FILE" $OPTIONS
