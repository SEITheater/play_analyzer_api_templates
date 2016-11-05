// Copyright Kevin M. Karol, 2016
// Provided under the MIT License to assist with image and metadata requests to PlayAnalyzer.com
// Please use these scripts in compliance with the site's Terms of Service
// and ensure that you have appropriate permissions before digitizing copyrighted texts

function errorHandler(jqXHR, status, error){
  console.log("Encountered post request error")
  console.log(status)
  console.log(error)
}

function makePostRequest(file, apiName, requestType, parameters, successCallback, errorCallback){
  apiURL = 'http://api.playanalyzer.com/' + apiName
  if(errorCallback == undefined){
    errorCallback = errorHandler
  }

  var formData = new FormData()
  formData.append('pml_text', file, 'pml_text')
  formData.append('type', requestType)
  for(var key in parameters){
    formData.append(key, parameters[key])
  }

  $.ajax({
      url: apiURL,
      type: 'POST',
      async: true,
      success: successCallback,
      error: errorCallback,
      // Form data
      data: formData,
      //Options to tell jQuery not to process data or worry about content-type.
      cache: false,
      contentType: false,
      processData: false
  });
}