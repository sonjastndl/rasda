# Author: Sonja Steindl 2023
# Status: in progress

# Executed python scripts to obtain data from OGC and match with DrosEU data 

###Get Information on the available layers as CSV file
python3 /media/ssteindl/fairicube/rasda/scripts/GetWCSlayerInfo.py

#takes an input (list of desired layers) and then defines the the minimum/common lat and lon boundaries 

#Original command
python3 scripts/GetBoundary.py --LayerInfoFile output/layer_info_WCS.csv -l AverageCholorColor -l AvgTemperatureColor -l mean_summer_airtemp
# Call the Python script and store its output as a Bash variable

output=$(python3 scripts/GetBoundary.py --LayerInfoFile output/layer_info_WCS.csv -l AverageCholorColor -l AvgTemperatureColor -l land_cover_class__esa_test_6 )

##neeed to include lat boundaries 27.0428:72.2158 !! ARE IN COMMAND BUT NOT IN SCRIPT 
python3 scripts/FilterSamples.py --source data/dest_v2.samps_25Feb2023.csv --boundary $output