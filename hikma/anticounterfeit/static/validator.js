function variableValidator (validationRule, inputElement, outputElement, validationMessage) {
	this.validationRule				= new RegExp(validationRule);
	this.inputElement				= inputElement;
	this.outputElement				= outputElement;
	this.validationMessage			= validationMessage;
	this.validationResult			= false;

	this.validateData = function() {
		if (this.validationRule.test(this.inputElement.val())) { //true
			this.validationResult	= true;
			this.validationMessage	= "";
		} else {
			this.validationResult	= false;
		}
		
		this.outputElement.html("<div class='variableValidator'><span class='variableValidator'>" + this.validationMessage	+ "</span></div>");
		return this.validationResult;
	};

	this.getValidationResult	= function() { return this.validationResult; };
	this.getValidationMessage	= function() { return this.validationMessage; };
};

function arrayValidator (variableValidatorArray) {
	this.variableValidatorArray = variableValidatorArray || [];
	this.arrayValidatorResult	= "True";
	
	this.validateArrayValidator = function() {
		for (arrayValidatorIndex = 0; arrayValidatorIndex < this.variableValidatorArray.length; arrayValidatorIndex++) {
			this.arrayValidatorResult = this.arrayValidatorResult && this.variableValidatorArray[arrayValidatorIndex].validateData();
		}
		return this.arrayValidatorResult;
	};
	
	this.arrayValidatorAddItem = function(arrayValidatorItem) {
		this.variableValidatorArray.push(arrayValidatorItem);
		//this.variableValidatorArray[variableValidatorArray.length] = arrayValidatorItem;
	};
	
};
