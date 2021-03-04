# ARMS DEALS AND CONFLICT DATA VIEWER

## INTRODUCTION
To run the entire program pipeline please run the "main.py" file. This file initiates the entire program and once activated it will trigger all subsequent files in the folder for a seamless program experience that will prompt the user to select available options. For this purpose, the program is divided into several modules based on different actions which are called from the main.py file. The user can access the full array of functionalities as he or she pleases, being able to return to previously available options throughout the running of the program. The program will run until the user decides to quit the program.

Users are invited to run the program several times using different inputs following the program's instructions.  This will allow the user to access limitless data selections based on time and several themes.  Furthermore, the user has several data visualization options at their disposal.  For maximum efficiency the program is designed to not re-download any data or repeat any computational functions when not necessary.

The program is divided in two main parts. The first part allows the user to access a general view on arms trade trends (TIV).  This component provides the user with the first visual glimpse into the data and the phenomenon at large.  The user is then able to continue with a deeper investigation in the second part of the program.
The second part is designed to render searchable (queried) table dashboards displaying arms trade deals and armed conflicts data.  Furthermore, the second part allows the user to create custom maps based on their data selections.

## OBJECTIVES
The purpose of this program is to provide the user with a self-contained pipeline, free of interruptions, to access, process, and visualize arms trade and armed conflict data on a global scale.  The capabilities of the program particularly focus on the quantities of weapons that are exchanged from a seller to a buyer (both, internationally recognized states and non-state actors).
The objective of this package is to facilitate the access to arms deals and conflict data.
The user can have a general view of arms trade deals data and further investigate specific arms deals and conflicts to best understand these interconnected phenomena.

Some standard questions that the program was set to answer:
1. Who are the main buyers and sellers of arms in a specific year or interval of years?
2. Are there armed conflicts that occurred in a certain region and at a time after certain arms trade deals?
3. What specific types of arms were sold by a certain state to another state or non-state actor in a particular year or interval of years, or in a certain transaction?

## DATA
The program is based on the following datasets:

From the Stockholm International Peace Research Institute (SIPRA):
1.   TIV data: trend-indicator values (transfer of military resources/capability) between 1950 and 2019. Data that gives a general idea about transfers (buying or selling) of arms.
2.   Trade Registers: each arms deal made between 1950 and 2019. More specific data where it is possible to verify specifically what each country (or armed group) bought or sold, and from or to whom.
More information here: https://www.sipri.org/sites/default/files/files/FS/SIPRIFS1212.pdf

And, from the Department of Peace and Conflict Research, Uppsala University, and from Centre for the Study of Civil Wars, International Peace Research Institute, Oslo:
3.   Armed conflict database: armed conflicts around the world between 1946 and 2019, with location and intensity of the conflict. The main unit in this dataset is a “State-based Armed Conflict” as defined by UCDP.
More information here: https://ucdp.uu.se/downloads/index.html#armedconflict

## SETTING THE ENVIRONMENT
The program was tested on two different operating systems: macOS and Microsoft Windows 10. In both instances, the scripts were written on the PyCharm integrated development environment (IDE).

For optimal performance, it is highly recommended for macOS users to set their environment through Anaconda and then set up an interpreter on the python 3.6 version. Additionally, macOS users can install the necessary packages directly on their hardware with python 3.9 version (the latest version available at the time of the development of this program), utilizing Brew.

For optimal performance, it is highly recommended for Windows 10 users to use pip (or pipwin) to install packages and use the python installed directly on their hardware as the interpreter, version 3.6 or a newer version.

If the user experiences difficulties installing geopandas on Windows 10 then the user should run the following sequence of installs using pipwin:

pip install wheel

pip install pipwin

pipwin install numpy

pipwin install pandas

pipwin install shapely

pipwin install gdal

pipwin install fiona

pipwin install pyproj

pipwin install six

pipwin install rtree

pipwin install geopandas

## COLAB
Google Colabatory(Colab) notebook for this program has been created and is available at:
https://colab.research.google.com/drive/1T0V0pWHzn91B0aHgE8Yr2jizJ2l14XEn?usp=sharing
The above colab link provides the user with a general overview of the program and allows the user to check specifics about the code and its outputs in "step-by-step" format.




