/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function(){
	$("#Product").load("http://127.0.0.1:8000/anticounterfeit/product");

	$("#PharmacyState").load("http://127.0.0.1:8000/anticounterfeit/state");
	$("#PharmacyState").change(function() {
		$("#PharmacyCity").load("http://127.0.0.1:8000/anticounterfeit/" + $("#PharmacyState").val() + "/city");
	});
	$("#PharmacyCity").change(function() {
		$("#Pharmacy").load("http://127.0.0.1:8000/anticounterfeit/" + $("#PharmacyCity").val() + "/pharmacy");
	});

	$("#DoctorState").load("http://127.0.0.1:8000/anticounterfeit/state/");
	$("#DoctorState").change(function() {
		$("#DoctorCity").load("http://127.0.0.1:8000/anticounterfeit/" + $("#DoctorState").val() + "/city");
	});
	$("#DoctorCity").change(function() {
		$("#Doctor").load("http://127.0.0.1:8000/anticounterfeit/" + $("#DoctorCity").val() + "/doctor");
	});
});
function selectedState(){
	$("#PharmacyState").val()
}
