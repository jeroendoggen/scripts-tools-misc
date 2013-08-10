#!/usr/bin/env bash
# A shell script to copy files over a local network using tar, netcat and pipes
# Written by: Jeroen Doggen (jeroendoggen@gmail.com)

while getopts p: option
do
        case "${option}"
        in
                p) PORT=${OPTARG};;
        esac
done

[ -z "$PORT" ] && echo "Usage: ''./receiver.sh -p port''" && exit

echo -ne "Listening on port: "
echo $PORT

nc -l $PORT | pv | tar -xvf -
