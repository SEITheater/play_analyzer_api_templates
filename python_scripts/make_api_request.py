# Copyright Kevin M. Karol, 2016
# Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
# Please use these scripts in compliance with the site's Terms of Service
# and ensure that you have appropriate permissions before digitizing copyrighted texts

# Adapted from http://stackoverflow.com/questions/68477/send-file-using-post-from-a-python-script

from convenience_variables import *
from os.path import isabs, isfile
import random
import string
import mimetypes
import urllib2
import httplib

def writeFileCallback(contents, relPath):
    global relativeOutputPath, metadataType
    f = open(relativeOutputPath + relPath, 'w')
    f.write(contents)
    f.close()

class MakeAPIRequest(object):
    def __init__(self, filePath, apiRequestType, postParams, dataReceivedCallback):
        self.filePath = filePath
        self.postParams = postParams
        global serverAddress
        self.dataReceivedCallback = dataReceivedCallback
        self.serverAddress = serverAddress + apiRequestType

    def makeRequest(self):
        self.upload_file(self.serverAddress, self.filePath)

    def random_string(self, length):
        return ''.join(random.choice(string.letters) for ii in range(length + 1))

    def encode_multipart_data(self, data, files):
        boundary = self.random_string(30)

        def get_content_type(filename):
            return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

        def encode_field(field_name):
            return ('--' + boundary,
                    'Content-Disposition: form-data; name="%s"' % field_name,
                    '', str(data[field_name]))

        def encode_file(field_name):
            filename = files[field_name]
            return ('--' + boundary,
                    'Content-Disposition: form-data; name="%s"; filename="%s"' % ('pml_text', filename),
                    'Content-Type: %s' % get_content_type(filename),
                    '', open(filename, 'rb').read())

        lines = []
        for name in data:
            lines.extend(encode_field(name))
        for name in files:
            lines.extend(encode_file(name))
        lines.extend(('--%s--' % boundary, ''))
        body = '\r\n'.join(lines)

        headers = {'content-type': 'multipart/form-data; boundary=' + boundary,
                   'content-length': str(len(body))}

        return body, headers

    def send_post(self, url, data, files):
        req = urllib2.Request(url)
        connection = httplib.HTTPConnection(req.get_host())
        connection.request('POST', req.get_selector(),
                           *self.encode_multipart_data(data, files))
        response = connection.getresponse()
        if(response.status == 200):
          self.dataReceivedCallback(response)


    def upload_file(self, server, path):
        assert isabs(path)
        assert isfile(path)

        data = {'MAX_FILE_SIZE': '3145728'}

        for key, val in self.postParams.iteritems():
            data[key] = val

        files = {'upfile': path}

        self.send_post(server, data, files)
