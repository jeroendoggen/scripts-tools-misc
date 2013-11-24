""" 
    Archive cleaner
    archiveCleaner.py is copyright 2013 Jeroen Doggen.
"""

import os
import sys
import shutil

scriptpath = os.getcwd()
inputfolder = scriptpath + "/input"
outputfolder = scriptpath + "/output"

def run():
    """Run the main program"""
    for directory, subdirectories, files in os.walk(inputfolder):
        for subdir in subdirectories:
            sourcedir = os.path.join(inputfolder, subdir)
            print(sourcedir)
            size = "%.2f" % float(get_size(sourcedir) / 1024 / 1024)
            shutil.move(sourcedir, outputfolder)
            if not os.path.exists(sourcedir):
                os.makedirs(sourcedir + "_backup_" + str(size) + "MB")

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return float(total_size)


if __name__ == "__main__":
    sys.exit(run())
