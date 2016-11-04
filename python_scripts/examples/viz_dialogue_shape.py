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
vizType = "dialogue_shape_chart"
#vizType = "line_shape_chart"
acts = ''
fromScene = '0'
toScene = '0'
characters = ''

def writeImageCallback(response):
    global characters, filePath, vizType
    imagePath = characters + "_" + vizType + ".png"
    writeFileCallback(response.read(), imagePath)

def makeChartForCharacter(filePath, characters):
  global vizType, acts, fromScene, toScene, apiRequestType

  postData = {
    'type': vizType,
    'acts': acts,
    'from_scene': fromScene,
    'to_scene': toScene,
    'characters': characters
  }

  request = MakeAPIRequest(filePath, apiRequestType, postData, writeImageCallback)
  request.makeRequest()


if __name__ == "__main__":
    makeChartForCharacter(absoluteFilePath, characters)