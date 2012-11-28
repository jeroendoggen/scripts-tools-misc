#!/bin/bash
##
#  Copyright 2011-2012 Jeroen Doggen (jeroendoggen@gmail.com)
#
#  Script to convert png/jpg bitmap images to pdf vector images (+upscaling)
#   - Usage: place images in 'images' folder, pdf version of images will be created in 'pdf' folder
#   - Depends on: tree, convert, potrace, epstopdf
##
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


##################################################################  
# SELECT FILES TO CONVERT                                        #
##################################################################
# Intermediate file extension (for 'temp' files)
ext='jpg'

# Selected file extensions
EXTS[0]='JPG'
EXTS[1]='gif'
EXTS[2]='jpeg'
EXTS[3]='png'
# Last element of the file extension array that is selected (only change when addding extra extensions)
LASTONE='3'

##################################################################  
# SCRIPT SETTINGS                                               #
##################################################################
threshold=0.90
resize=3000

# Helper variables
count=0


##################################################################  
# FUNCTIONS                                                      #
##################################################################

function createFolders
{
# Create 'pdf' folder if it does not exist
tree -d | grep pdf > /dev/null
if [ $? -eq 1 ] 
  then 
    mkdir pdf
fi

# Create 'pdf' folder if it does not exist
tree -d | grep images > /dev/null
if [ $? -eq 1 ] 
  then 
    mkdir temp
fi
}

# Convert images with various extension to .jpg images
function convertTo_jpg
{
cd images
for ((i=0;i<=LASTONE;i++)); do
    for f in $(find -type f -iname "*.""${EXTS[i]}" )
    do
      dest=`echo ${f%.*}`
      echo "Convert from : '$dest.${EXTS[i]}' to '$dest.$ext'"
      convert "${f}" "${dest}.jpg"
      if [ "${EXTS[i]}" == "$ext" ]
        then
          cp "${dest}.jpg" ../temp
        else 
          cp "${dest}.jpg" ../temp
      fi
   done
done
}

function convertTo_pdf
{
cd images
for ((i=0;i<=LASTONE;i++)); do
# Convert *.jpg to *.pdf (+filtering)
  for f in $(find -type f -iname '*.'"${EXTS[i]}" )
  do
      dest=`echo ${f%.*}`
      echo "Converting to pdf: $dest.${EXTS[i]}"
      let count=count+1
      convert -resize $resize -quality 100% "${f}" "../pdf/${dest}.jpg"
      convert -resize $resize -quality 100% "${f}" "../pdf/${dest}.bmp"
      mkbitmap "../pdf/${dest}.bmp" -f 10 -o "../pdf/${dest}.bmpout"       #low pass filter (remove slow gradients from scans)
      potrace -k $threshold -r 100 "../pdf/${dest}.bmpout"              #convert to eps
      epstopdf "../pdf/${dest}.eps"	              			    #convert to pdf
      rm "../pdf/${dest}.bmp"
      rm "../pdf/${dest}.bmpout"
      rm "../pdf/${dest}.jpg"
      rm "../pdf/${dest}.eps"
  done
done

}

function printLog
{
echo "$count images have been converted"
}

##################################################################  
# "MAIN CODE" STARTS HERE                                        #
##################################################################

createFolders
convertTo_pdf
printLog
