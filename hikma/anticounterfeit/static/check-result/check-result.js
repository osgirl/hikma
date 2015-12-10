$(document).ready(function(){
	$("#product").load("/anticounterfeit/product");

	$("#pharmacyState").load("/anticounterfeit/state");
	$("#pharmacyState").change(function() {
		$("#pharmacyCity").load("/anticounterfeit/" + $("#pharmacyState").val() + "/city");
	});
	$("#pharmacyCity").change(function() {
		$("#pharmacy").load("/anticounterfeit/" + $("#pharmacyCity").val() + "/pharmacy");
	});

	$("#doctorState").load("/anticounterfeit/state");
	$("#doctorState").change(function() {
		$("#doctorCity").load("/anticounterfeit/" + $("#doctorState").val() + "/city");
	});
	$("#doctorCity").change(function() {
		$("#doctor").load("/anticounterfeit/" + $("#doctorCity").val() + "/doctor");
	});
	$("#check").click(function() {
		postArray = {
			product : $("#product").val()
		}
		$.post("/anticounterfeit/result/", postArray, function(data, status){
			$("#bodyDiv").html(data)
			/*alert("Status: " + status);*/
		});
	});
});
