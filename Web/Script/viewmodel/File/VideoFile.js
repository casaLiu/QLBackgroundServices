/**
*@author: casa
*
*@date: 2014-08-28
*
*@note: FileModel
*
*/
(function(vm){
	vm["FileInfo"] = ko.mapping.fromJS({
		name : '',
		fullname : '',
		audioFormat : '',
		encoding : '',
		rate : '',
		audioChannel : '',
		httpBaseUrl : ''
	});
})(this.ViewModel);