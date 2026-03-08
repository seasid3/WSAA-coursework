# This program prints the data for all trains in Ireland to the console.
# Author: Orla Woods

import requests
import csv
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page =  requests.get(url)
doc = parseString(page.content)
# check it works
# print (doc.toprettyxml()) #output to console

# if I want to store the xml in a file, can comment out later
#with open("currenttrains.xml", "w") as xmlfp:
#    doc.writexml(xmlfp)

# print out each of the trainscodes. i.e. find listings and iterate
# through them to frint each traincode out. 

# retrieve tags
retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',   
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction',
                ]
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode =  traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

# modify to print out the latitudes
with open("currenttrains.csv", mode = "w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter = "\t", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    objTrainPosititionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        # create an array called dataList, append in traincode and sore in the CSV.
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)