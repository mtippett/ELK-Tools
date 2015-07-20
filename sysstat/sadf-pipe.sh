#!/bin/sh

_path=`dirname $0`
_file=$1

if [ "${_file}" != "" ]; then
  if [ ! -r "${_file}" ]; then
     echo "Not able to find sar file ${_file}"
     exit 1
  fi
fi	


sadf  ${_file} -j -- -A | ${_path}/morph-sar.py


