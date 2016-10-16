function downloadAPK(){
//	window.open("/protected/10-13-2016-0.csv");
	
	$.ajax({
		type: "GET",
		url: "http://cxp.sytes.net/dataplot",
		dataType: "json",
		async: true,
		data: {
			downloadFile: "yes",
			filename:"cxp-apk",
		},
	});
	
}

function downloadCSVFile(){
	$.ajax({
		type: "GET",
		url: "http://cxp.sytes.net/dataplot",
		dataType: "json",
		async: true,
		data: {
			downloadFile: "yes",
			filename: fname,
		},
	});	
}
/*
function getChart(fname, label) {
	$.ajax({
		type: "GET",
		url: "http://cxp.sytes.net/dataplot",
		dataType: "json",
		async: true,
		data: {
			filename:fname,
			metric: label,
		},
		success: function(data) {
			makeChart(data);
		},
		error: function() {
			alert('File does not exist');
		},
	});
}

function makeChart(json_data) {
	var data_var = {
		labels:json_data['stamps'],
		datasets: [
		{
			label: "Resistance",
			fill: false,
			pointBackgroundColor: "#fff",
			data: json_data['csv_data'],
		}
		]
	}
	var ctx = $("#myChart").get(0).getContext("2d");
	//var ctx = document.getElementById("myChart").get(0).getContext("2d");
	new Chart(ctx, {
		type: "line",
	    	data: data_var,
	});
}*/
