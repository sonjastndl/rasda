## RASDA 
This repository is supposed to hold documentation on a future element of the "Landscape Genomics Pipeline" used for the UC3 Project of FAIRiCUBE. The Rasda repository is building the framework for  "Wormpicker" (UDF) of UC3.

Currently the OGC Service used is provided by rasdaman (https://ows.rasdaman.org/rasdaman/ows#/services).

The main workflow established is executed by several python scripts manually, this worklfow is documented in a [main file](main.sh). 


## Repository Structure

- **Data:** Holding input data for filtering. Filtering is implemented, so only layers are used that match with sample coordinates.  
- **Scripts:** All python scripts that will in the end form the function are stored in[scripts](/scripts).
- **Output:** Is storing all intermediate files. 
- **Results:** Will store results of this workflow. 

## Workflow

### Data

**Sample-Metafile** The file [samps.csv](data/dest_v2.samps_25Feb2023.csv) is holding the information where the samples were taken in lat/long coordinate form and stores additional metadata. The tablecan be downloaded from DESTbio (https://dest.bio/).


### Scripts

in progress



### Output

in progress



### Results

Soon :-)