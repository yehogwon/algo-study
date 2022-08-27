#!/bin/sh

BASEDIR=$(dirname "$0") # the relative location of the script file

if [ $# -eq 0 ]
  then
    echo "Arguments are required"
else
  cd "${BASEDIR}/cracking-the-coding-interview"
  for arg in "${@:3}"
    do
      mkdir "CH${2}/$arg"
      cp "../template/tem.${1}" "CH${2}/$arg/$arg.${1}"
      echo "$arg"
    done
  cd - >> /dev/null
fi
