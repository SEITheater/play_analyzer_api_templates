# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

import sys
sys.path.append('..')
from make_api_request import *

# This file uses convenience variables set in convenience_variables.py
# be sure to set the filePath variable to make requests

metadataType = "character_speech_flow"
apiRequestType = "metadata"

acts = ''
fromScene = '0'
toScene = '0'
characters = ''

def callback(response):
    global metadataType
    import json
    responseArray = json.loads(response.read())
    outputString = "Who speaks after whom?\n"

    for entry in responseArray:
        outputString += entry["character_1"] + " then " + entry["character_2"] + " " + \
                        str(entry["count"]) + " times which is " + str(entry["percentage"]) + "%\n"

    writeFileCallback(outputString, metadataType + ".txt")



def getCharacterList(filePath):
  global metadataType, apiRequestType, acts, fromScene, toScene, characters

  postData = {
    'type': metadataType,
    'acts': acts,
    'from_scene': fromScene,
    'to_scene': toScene,
    'characters': characters
  }

  request = MakeAPIRequest(filePath, apiRequestType, postData, callback)
  request.makeRequest()


if __name__ == "__main__":
    getCharacterList(absoluteFilePath)