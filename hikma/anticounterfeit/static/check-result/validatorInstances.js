function validateDataFunction(){
	$("[validator]").change(function(){
		var vv = new variableValidator($(this));
		vv.validateData();
	});
}
function validateArrayValidatorFunction() {
	var av = new arrayValidator();
	$("[validator]").each(function() {
		var vv1 = new variableValidator($(this));
		vv1.validateData();
		av.arrayValidatorAddItem(vv1);
	});
	return av.validateArrayValidator();
}
