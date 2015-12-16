function variableValidator (validationRule, inputElement, outputElement) {
	
	this.validationRule				= validationRule;
	this.validationRules			= { "^Required":"^$", 
										"CapitalAndSmallEnglish-Arabic-Space":"[^ a-zA-Z\u0621-\u063A\u0641-\u064A]|^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{1,2}$|^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{51,}$|[ ][ ]",
										"CapEn":"[^A-Z]+", "CapEn04-06":"^[A-Z]{1,3}$|^[A-Z]{7,}$", 
										"Ar-Space":"[^\u0621-\u063A\u0641-\u064A\u0020]+", 
										"Digits":"[^0-9]+", "Digits04-09":"^[0-9]{1,3}$|^[0-9]{10,}$"};
										
	this.validationRulesMessages	= { "CapitalAndSmallEnglish-Arabic-SpaceWrong":"من فضلك ادخل حروف عربية, إنجليزية أو مسافة بحد أدنى 2 حرف وحد أقصى 50 حرف حيث يسمج بمسافة واحدة بين كل كلمة والأخرى", "CapitalAndSmallEnglish-Arabic-SpaceRight":"",
										"^RequiredWrong":"من فضلك هذه قيمة مطلوبة يجب إدخالها", "^RequiredRight":"", 
										"CapEnWrong":"حروف إنجليزية كبيرة", "CapEnRight":"",
										"CapEn04-06Wrong":"من 4 إلى 6 حروف إنجليزية كبيرة", "CapEn04-06Right":"",
										"Ar-SpaceWrong":"حروف عربية ومسافة فقط", "Ar-SpaceRight":"",
										"DigitsWrong":"أرقام فقط", "DigitsRight":"",
										"Digits04-09Wrong":"من 4 إلى 6 أرقام فقط", "Digits04-09Right":"" };
										
										
	this.inputElement				= inputElement;
	this.outputElement				= outputElement;
	this.outputMessage				= "";
	this.validationResult			= false;

	this.validateData = function() {
		for (validationRuleKey in this.validationRules) {
			validationRuleKeyRegExpObject			= new RegExp(validationRuleKey);
			isValidationRuleActivatedOnThisInput	= validationRuleKeyRegExpObject.test(this.validationRule);
			if (isValidationRuleActivatedOnThisInput) {
				validationRulePattern 				= this.validationRules[validationRuleKey];
				validationRulePatternRegExpObject	= new RegExp(validationRulePattern);
				if (validationRulePatternRegExpObject.test(this.inputElement.val())) { //true
					this.validationResult	= false;
					this.outputMessage		= this.validationRulesMessages[validationRuleKey+"Wrong"];
					break;
				} else {
					this.validationResult	= true;
					this.outputMessage		= this.validationRulesMessages[validationRuleKey+"Right"];
				}
			}
		}
		this.outputElement.html("<div><span class='validatorResult'>" + this.outputMessage	+ "</span></div>");
		return this.validationResult;
	};
	
	this.getValidationResult	= function() { return this.validationResult; };
	this.getoutputMessage		= function() { return this.outputMessage; };
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
