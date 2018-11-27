import os, re
import csv 
import logging
# from log import log
logging.basicConfig(filename="hey.log", filemode="w", level=logging.DEBUG)

prjPath = r"\\vpp-revit01\D$\Revit Server 2017\Projects\0110_Западный Порт\Корпус 01\30_АР"
# Retrieve all element in RSN directory  
with open(r"C:\Users\malozyomovvv\Desktop\CheckProjectFilePathLength\out.txt", "w", encoding="utf-8") as csvFile:
    # writer = csv.writer(csvFile)
    data = []
    for root, folders, files in os.walk(prjPath):
        for folder in folders:
            if ".rvt" in root or ".rvt" in folder:
                folderPath = os.path.join(root, folder)
                # logging.debug(folderPath)
                print(folderPath[14:])
                print(str(len(folderPath)))
                # data.append(folderPath + "\n")
                csvFile.write(folderPath[14:] + "\n")

                
    # writer.writerows(data)