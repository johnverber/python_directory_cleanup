import os

myList = [".msi", ".msm", ".msp", ".mst", ".idt", ".idt", ".cub", ".pcp", ".exe"]


rootDir = '.'
for dirName, subdrList, fileList in os.walk(rootDir):
    print('Found directory: %s' %dirName)
    for fileName in fileList:
        for extName in myList:
            if(fileName.endswith(extName)):
                    print('\t Deleting %s' % fileName)
                    os.remove(os.path.join(dirName, fileName))
                    break