#!/bin/sh 
# Indenter.sh : automatic source code indentation
# Depends on: bcpp, bash 
# Copyright 2012 Jeroen Doggen (jeroendoggen@gmail.com)

if [ ! -n "$1" ]; then
  echo "Syntax is: recurse.sh dirname filesuffix"
  echo "Syntax is: recurse.sh filename"
  echo "Example: recurse.sh temp cpp"
  exit 1
fi

if [ -d "$1" ]; then
  if [ -n "$2" ]; then
    filesuffix=$2
  else
    filesuffix="*"
  fi

  file_list=`find ${1} -name "*.${filesuffix}" -type f`
  
  for file2indent in $file_list
    do 
      echo "Indenting file $file2indent"
      #!/bin/bash
      bcpp -fi "$file2indent" -fnc "bcpp_indenter.cfg" -fo indentoutput.tmp
      mv indentoutput.tmp "$file2indent"
    done
else
  if [ -f "$1" ]; then
    echo "Indenting one file $1"
    #!/bin/bash
    bcpp -fi "$1" -fnc "bcpp_indenter.cfg" -fo indentoutput.tmp
    mv indentoutput.tmp "$1"
  else
    echo "ERROR: As parameter given directory or file does not exist!"
    echo "Syntax is: call_BCPP.sh dirname filesuffix"
    echo "Syntax is: call_BCPP.sh filename"
    echo "Example: call_BCPP.sh temp cpp"
    exit 1
  fi
fi
