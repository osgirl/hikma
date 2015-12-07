/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function(){
	$("#PharmacyState").load("http://127.0.0.1:8000/anticounterfeit/state/");
});
function addRow(tableID){
    var tr=$('<tr><td></td><td></td><td></td><td><button onclick="removeRow(this)">-</button></td></tr>').appendTo($("#"+tableID));
    for(var i=0;i<3;i++){$(tr).children("td").eq(i).text($("select").eq(i).val());}
    //var tr=$('<tr><td><button onclick="removeRow(this)">-</button></td></tr>').appendTo($("#"+tableID));
    //for(var i=2;i>-1;i--){$(tr).prepend($("<td>" + $($("select")[i]).val() + "</td>"));}
}
function removeRow(removeRowButtonObject){
    $(removeRowButtonObject).parents("tr").remove();
}
