#!/usr/bin/env python3

"""
    json_merge.py: tool to merge .json & .jpeg folder from Google Photos exports
    json_merge.py is copyright 2020 Jeroen Doggen.
"""


import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="the folder that should be processed")
args = parser.parse_args()

file_counter = 0

print("\nMerging .json & .jpg files...")
for subdir, dirs, files in os.walk(args.folder):
    for filename in files:
        filepath = subdir + os.sep + filename

        json_end_string = ").json"
        jpeg_end_string = ".jpg"

        if filepath.endswith(json_end_string):
            # print("JPEG file: " + filename)

            base_name = filename.rstrip(json_end_string)

            last = ""
            number = ""

            while base_name.__len__() > 0:
                last = base_name[-1:]
                base_name = base_name[:-1]
                if last is '(':
                    break
                else:
                    number += last

            try:
                number = int(number)
            except:
                print("Invalid number: " + str(number))

            if base_name.endswith(jpeg_end_string):
                # print("JPEG base name: " + base_name)
                base_name = base_name.rstrip(jpeg_end_string)

                new_name = base_name + '(' + str(number) + ')' + ".jpg.json"
                # print("New name: " + new_name)

                filepath_new = subdir + os.sep + new_name

                try:
                    shutil.copyfile(filepath, filepath_new)
                    print(str(file_counter+1) + ". Copied: " + filepath + " --> " + filepath_new)
                    file_counter += 1
                except:
                    print("Copy failed: " + filepath)

print("Number of merged files: " + str(file_counter))

merge_cmd = "exiftool -r -d %s -tagsfromfile \"%d/%F.json\" " \
            "\"-GPSAltitude<GeoDataAltitude\" \"-GPSLatitude<GeoDataLatitude\" " \
            "\"-GPSLatitudeRef<GeoDataLatitude\" \"-GPSLongitude<GeoDataLongitude\" " \
            "\"-GPSLongitudeRef<GeoDataLongitude\" \"-Keywords<Tags\" " \
            "\"-Subject<Tags\" \"-Caption-Abstract<Description\" " \
            "\"-ImageDescription<Description\" \"-DateTimeOriginal<PhotoTakenTimeTimestamp\" " \
            "-ext jpg -overwrite_original "

print(merge_cmd + args.folder)
retVal = os.system(merge_cmd + args.folder)
