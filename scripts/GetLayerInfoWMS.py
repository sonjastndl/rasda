import requests
import csv
import xml.etree.ElementTree as ET

# Define the URL for the GetCapabilities operation
## needs to be changed to "fairicube:rasda:ows...blabla" aka the real fairicube rasdaman database 
url = "https://ows.rasdaman.org/rasdaman/ows?service=WMS&request=GetCapabilities"
url = "https://ows.rasdaman.org/rasdaman/ows?service=WCS&request=GetCapabilities"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Parse the response content as an ElementTree object
tree = ET.fromstring(response.content)

# Find all Layer elements in the capabilities document
layers = tree.findall(".//{http://www.opengis.net/wms}Layer")

# Create a list to store the layer names and bounding boxes
layer_info = []

# Loop through the Layer elements and extract the layer name and bounding box
for layer in layers:
    name = layer.findtext("{http://www.opengis.net/wms}Name")
    bbox = layer.find("{http://www.opengis.net/wms}BoundingBox")
    print(bbox)
    dim = layer.findtext("{http://www.opengis.net/wms}Dimension[@name='time']")
    if bbox is not None and dim is not None:
        minx = bbox.get("minx")
        miny = bbox.get("miny")
        maxx = bbox.get("maxx")
        maxy = bbox.get("maxy")
        times = dim.split(",")
        start_time = times[0]
        end_time = times[-1]
        layer_info.append((name, minx, maxx, miny, maxy, start_time, end_time))

# Write the layer names and bounding boxes to a CSV file
with open("/media/ssteindl/fairicube/rasda/output/layer_info_WCS.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["LayerName", "Min X", "Max X", "Min Y", "Max Y", "TimeStart", "TimeEnd"])
    writer.writerows(layer_info)

