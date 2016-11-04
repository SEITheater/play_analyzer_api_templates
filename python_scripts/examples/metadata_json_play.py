# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

import sys
sys.path.append('..')
from make_api_request import *

# This file uses convenience variables set in convenience_variables.py
# be sure to set the filePath variable to make requests

metadataType = "parsed_play_list"
apiRequestType = "metadata"


def callback(response):
    global metadataType
    writeFileCallback(response.read(), metadataType + ".txt")

def getEntryList(filePath):
  global metadataType, apiRequestType

  postData = {
    'type': metadataType
  }

  request = MakeAPIRequest(filePath, apiRequestType, postData, callback)
  request.makeRequest()


if __name__ == "__main__":
    getEntryList(absoluteFilePath)