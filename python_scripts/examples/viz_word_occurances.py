# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

import sys
sys.path.append('..')
from make_api_request import *

# This file uses convenience variables set in convenience_variables.py
# be sure to set the filePath variable to make requests

apiRequestType = "generate_viz"
vizType = "word_occurances_chart"

acts = ''
fromScene = ''
toScene = ''
characters = ''
words = []


def writeImageCallback(response):
    global vizType, words
    imagePath = vizType + "_"
    for word in words:
        imagePath += word + "_"
    imagePath += ".png"

    writePNGCallback(response.read(), imagePath)


def makeChartForCharacter(filePath):
  global apiRequestType, vizType, acts, fromScene, toScene, characters, words

  postData = {
    'type': vizType,
    'from_scene': fromScene,
    'to_scene': toScene,
    'acts' : acts,
    'characters': characters,
    'words': words
  }

  request = MakeAPIRequest(filePath, apiRequestType, postData, writeImageCallback)
  request.makeRequest()

if __name__ == "__main__":
    makeChartForCharacter(absoluteFilePath)