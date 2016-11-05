# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

import sys
sys.path.append('..')
from make_api_request import *
import json

# This file uses convenience variables set in convenience_variables.py
# be sure to set the filePath variable to make requests

apiRequestType = "available_request_types"


def callback(response):
    global apiRequestType
    requestTypeList = json.loads(response.read())
    outputString = ""

    for entry in requestTypeList:
        outputString += "{"
        outputString += "\n"
        for key, value in entry.iteritems():
            outputString += "    "
            outputString += json.dumps(key)
            outputString += ":"
            outputString += json.dumps(value)
            outputString += ","
            outputString += "\n"
        outputString += "},"
        outputString += "\n\n"


    writeFileCallback(outputString, apiRequestType + ".txt")

def getRequestTypes(filePath):
  global apiRequestType

  postData = {
  }

  request = MakeAPIRequest(filePath, apiRequestType, postData, callback)
  request.makeRequest()

if __name__ == "__main__":
    getRequestTypes(absoluteFilePath)