#!/usr/bin/env bash
# A shell script to copy files over a local network using tar, netcat and pipes
# Written by: Jeroen Doggen (jeroendoggen@gmail.com)


while getopts s:d:p: option
do
        case "${option}"
        in
                s) SOURCE=${OPTARG};;
                d) DESTINATION=${OPTARG};;
                p) PORT=${OPTARG};;
        esac
done

[ -z "$PORT" ] || [ -z "$DESTINATION" ] || [ -z "$SOURCE" ]   && echo "Usage: ''./sender.sh -s source_folder -d destination_host -p port''" && exit

echo -ne "Source folder: "
echo $SOURCE

echo -ne "Destination host: "
echo -ne $DESTINATION
echo -ne " port: "
echo $PORT

tar c --remove-files $SOURCE |  nc $DESTINATION $PORT