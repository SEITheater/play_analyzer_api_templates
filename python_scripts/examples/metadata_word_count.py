# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

import sys
sys.path.append('..')
from make_api_request import *

# This file uses convenience variables set in convenience_variables.py
# be sure to set the filePath variable to make requests

metadataType = "most_common_words"
apiRequestType = "metadata"

acts = ''
fromScene = '0'
toScene = '0'
characters = ''

#source https://www.englishclub.com/vocabulary/common-words-100.htm
mostCommonWords = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with",
                   "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her",
                   "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out",
                   "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just",
                   "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other",
                   "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use",
                   "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these",
                   "give", "day","most", "us"]


def callback(response):
    global mostCommonWords, metadataType
    import json
    responseArray = json.loads(response.read())
    outputString = ""

    for entry in responseArray:
        if entry["word"] not in mostCommonWords:
            outputString += entry["word"] + "-" + str(entry["count"]) + "\n"

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