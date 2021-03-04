import sys, wget, zipfile, os, shutil
from urllib.request import urlopen

print("\nWait until the process is finished: ")

def bar_progress(current, total, width):
  progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total,)
#We decided to not use print() as it will print in new line every time, redundant
  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()

zipurl = wget.download( "https://gisco-services.ec.europa.eu/distribution/v2/countries/download/ref-countries-2020-01m.shp.zip",
               bar=bar_progress )
#Downloads the file from the URL
zipresp = urlopen("https://gisco-services.ec.europa.eu/distribution/v2/countries/download/ref-countries-2020-01m.shp.zip")
#Creates a new file on the hard drive
tempzip = open("ref-countries-2020-01m.shp.zip", "wb")
#Writes the contents of the downloaded file into the new file
tempzip.write(zipresp.read())
#Closes the newly-created file
tempzip.close()
#Reopens the newly-created file with ZipFile()
zf = zipfile.ZipFile("ref-countries-2020-01m.shp.zip")
# Extract its contents into <extraction_path>
#Extractall will automatically create the path
zf.extractall(path = "border_countries_extracted")
zf.close()

zf = zipfile.ZipFile("border_countries_extracted/CNTR_LB_2020_3857.shp.zip")
zf.extractall( path ='0-Downloaded_files/centroid_by_world_state' )
zf.close()

zf = zipfile.ZipFile("border_countries_extracted/CNTR_RG_01M_2020_3857.shp.zip")
zf.extractall( path ="0-Downloaded_files/borders_world" )
zf.close()

shutil.rmtree("border_countries_extracted")
os.remove("ref-countries-2020-01m.shp.zip")