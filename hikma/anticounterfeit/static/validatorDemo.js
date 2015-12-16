$(document).ready(function(){
	validateDataFunction();
});

function validateDataFunction(){
	$("[validator]").each(function(){
		var vv = new variableValidator($(this));
		vv.validateData();
	});
	
	$("[validator]").on("change input keyup paste propertychange", function(){
		var vv = new variableValidator($(this));
		vv.validateData();
	});
}

/*function validateArrayValidatorFunction() {
	var vv1 = new variableValidator("^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{3,50}$", $("#textInput"), "حروف عربية, إتجليزية أو مسافة واحدة بين كل كلمة والأخرى");
	vv1.validateData();
	
	var av = new arrayValidator();
	av.arrayValidatorAddItem(vv1);
	alert(av.validateArrayValidator());
}*/
