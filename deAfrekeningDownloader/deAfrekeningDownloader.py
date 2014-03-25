"""
    deAfrekeningDownloader.py: a tool to download the latest 'de Afrekening'
      podcast from the web.
    deAfrekeningDownloader.py is copyright 2014 Jeroen Doggen.
"""

import os
import sys
import urllib2
import urllib

SCRIPTPATH = os.getcwd()
OUTPUTFOLDER = SCRIPTPATH + "/downloads"

RSS_FILE = "http://internetradio.vrt.be/podcast/StuBru/rss-41_dafr.xml"


def run():
    """Run the main program"""
    response = urllib2.urlopen(RSS_FILE)
    html = response.read()

    for item in html.split("\n"):
        if "http://download.streampower.be" in item:
            item = item.lstrip()
            item = item.lstrip("<enclosure url=\"")
            item = item.rstrip()
            mp3link = item[0:67]
            mp3file = item[43:67]
            print ("Downloading: " + mp3file)
    urllib.urlretrieve(mp3link, mp3file, reporthook=show_progress)


def show_progress(count, blockSize, totalSize):
    """ Show a progress counter """
    percent = int(count * blockSize * 100 / totalSize)
    sys.stdout.write("%2d%%" % percent)
    sys.stdout.write("\b\b\b")
    sys.stdout.flush()

if __name__ == "__main__":
    sys.exit(run())
