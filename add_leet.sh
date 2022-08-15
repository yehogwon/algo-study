#!/bin/sh

BASEDIR=$(dirname "$0") # the relative location of the script file

if [ $# -eq 0 ]
  then
    echo "Arguments are required"
else
  cd "${BASEDIR}/leetcode"
  for arg in "${@:2}"
    do
      mkdir "$arg"
      touch "$arg/$arg.${1}"
      echo "$arg"
    done
  cd - >> /dev/null
fi
