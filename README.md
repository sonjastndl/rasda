## RASDA 
This repository is supposed to hold documentation on a future element of the "Landscape Genomics Pipeline" used for the UC3 Project of FAIRiCUBE. The Rasda repository is building the framework for  "Wormpicker" (UDF) of UC3.

Currently the OGC Service used is provided by rasdaman (https://ows.rasdaman.org/rasdaman/ows#/services).

The main workflow established is executed by several python scripts manually, documented compact in a [main file](main.sh) with execution code, further explanation and backround can be read under [Workflow](#workflow). 


## Requirements



## Repository Structure

- **Data:** Holding input data for filtering. Filtering is implemented, so only layers are used that match with sample coordinates.  
- **Scripts:** All python scripts that will in the end form the function are stored in [scripts](/scripts).
- **Output:** Is storing all intermediate files. 
- **Results:** Will store results of this workflow. 

## Workflow

### Data

**Sample-Metafile** The file [samps.csv](data/dest_v2.samps_25Feb2023.csv) is holding the information where the samples were taken in lat/long coordinate form and stores additional metadata. The tablecan be downloaded from DESTbio (https://dest.bio/).


### Scripts

**GetWCSlayerInfo.py** This [script](scripts/GetWCSlayerInfo.py) is currently manually accessing ows.rasdaman.org and creates a short description file for GetCapabilities, more specific a csv table with information on all layers provided (name, geo extent and time dimensions) which can be found [here](output/layer_info_WCS.csv).

**GetBoundary.py** This [script](scripts/GetBoundary.py) is designed to find the "minimal overlapping area" of all the layers of interest (provided by a list with paramter -l). The idea is to allow inclusion of all metavariables to all later sample analysis to the same extent.

It is called via shell command and stores minimum and maximum for latitude and longitude in a variable called *output*. This will be used in the next python code. 

**FilterSamples.py** Uses the *output* as reference to filter out samples from [samps.csv](data/dest_v2.samps_25Feb2023.csv), so only sampels that are covered by these layers of interest will be processed. The scripts can be found [here](scripts/FilterSamples.py). 

*Ideally this can be expanded with a method that defines the combination of layers where the most samples are covered to increase meaningfulness of the analysis.*

**GetData.py** In Progress.


### Output

in progress



### Results

Soon :-)