import sys
import wget
from urllib.request import urlopen
import zipfile
import os


def bar_progress(current, total, width=80):
  progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)

#NOTE: DON'T USE PRINT() AS IT WILL PRINT IN NEW LINE EVERY TIME.

  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()

zipurl = wget.download( "https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-201-csv.zip", bar=bar_progress )

#DOWNLOADS THE FILE FROM THE URL

zipresp = urlopen("https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-201-csv.zip")

#CREATES A NEW FILE ON THE HARD DRIVE

print("\nWait until the process is finished: ")
tempzip = open("ucdp-prio-acd-201-csv.zip", "wb")

#WRITES THE CONTENTS OF THE DOWNLOADED FILE INTO NEW FILE

tempzip.write(zipresp.read())

#CLOSES THE NEWLY CREATED FILE

tempzip.close()

#REOPENS THE NEWLY-CREATED FILE WITH ZIPFILE()

zf = zipfile.ZipFile("ucdp-prio-acd-201-csv.zip")

#EXTRACT ITS CONTENTS <extraction_path>
#EXTRACTALL WILL AUTOMATICALLY CREATE THE PATH

zf.extractall( path ='0-Downloaded_files/ucdp-prio-acd-201-csv' )
zf.close()
os.remove("ucdp-prio-acd-201-csv.zip")




