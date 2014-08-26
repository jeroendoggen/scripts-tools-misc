"""
    WualaCleaner: tool to clean up "fotos-familie" archive
    WualaCleaner.py is copyright 2013,2014 Jeroen Doggen.
"""

import os
import sys
import shutil


SCRIPTPATH = os.getcwd()
INPUTFOLDER = SCRIPTPATH + "/input"
OUTPUTFOLDER = SCRIPTPATH + "/output"


def run():
    """Run the main program"""
    print("Moving files to output folder & creating lowres versions...")
    for directory, subdirectories, files in os.walk(INPUTFOLDER):
        print(directory)
        for thefile in files:
            os.chdir(directory)
            if not "_lowres" in thefile:
                outputfile = thefile + "_lowres.jpg"
                os.system("convert -gaussian-blur 0.03 -quality 75% -resize 1280"
                            + " " + thefile
                            + " " + outputfile)
                dirs = os.path.split(directory)
                dirs = dirs[1]
                target = os.path.join(OUTPUTFOLDER, dirs)
                print("Creating: " + dirs + "/" + outputfile)
                if not os.path.exists(target):
                    os.mkdir(target)
                if os.path.exists(outputfile):
                    shutil.move(outputfile, target + "/" + outputfile)
            os.chdir(INPUTFOLDER)


def get_size(start_path='.'):
    """ Calculate folder size """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for inputfile in filenames:
            filepointer = os.path.join(dirpath, inputfile)
            total_size += os.path.getsize(filepointer)
    return float(total_size)


if __name__ == "__main__":
    sys.exit(run())
