(function() {
    var prevOnError = window.onerror;
    window.onerror = function (errorMsg, url, lineNumber) {
	if (typeof(jQuery) != 'undefined') {
	    jQuery.ajax({ url: '/jhouston/onerror/',
			  type: 'POST',
			  data: {
			      message: errorMsg,
			      line_number: lineNumber,
			      url: url
			  }
			});
	}
	if (prevOnError) {
	    return prevOnError(errorMsg, url, lineNumber);
	}
	return false;
    }
})();