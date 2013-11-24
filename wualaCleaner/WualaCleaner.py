""" 
    WualaCleaner: tool to clean up "fotos-familie" archive
    WualaCleaner.py is copyright 2013 Jeroen Doggen.
"""

import os
import sys
import shutil

SCRIPTPATH = os.getcwd()
INPUTFOLDER = SCRIPTPATH + "/input"
OUTPUTFOLDER = SCRIPTPATH + "/output"

def run():
    """Run the main program"""
    for directory, subdirectories, files in os.walk(INPUTFOLDER):
        for subdir in subdirectories:
            sourcedir = os.path.join(INPUTFOLDER, subdir)
            print(sourcedir)
            size = "%.1f" % float(get_size(sourcedir) / 1024 / 1024)
            shutil.move(sourcedir, OUTPUTFOLDER)
            if not os.path.exists(sourcedir):
                os.makedirs(sourcedir + "_backup_" + str(size) + "MB")

def get_size(start_path = '.'):
    """ Calculate folder size """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for inputfile in filenames:
            filepointer = os.path.join(dirpath, inputfile)
            total_size += os.path.getsize(filepointer)
    return float(total_size)


if __name__ == "__main__":
    sys.exit(run())
