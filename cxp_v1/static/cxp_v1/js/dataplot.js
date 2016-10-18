function getChart(fname, mlabel) {
	$.ajax({
		type: "GET",
		url: "http://cyclexpro.com/dataplot",
		dataType: "json",
		async: true,
		data: {
			downloadFile: "no",
			filename:fname,
			metric: mlabel,
		},
		success: function(data) {
			makeChart(data, mlabel);
		},
		error: function() {
			alert('File does not exist');
		},
	});
}

function makeChart(json_data, metric) {
	var data_var = {
		labels:json_data['stamps'],
		datasets: [
		{
			label: metric,
			fill: false,
			pointBackgroundColor: "#888",
			data: json_data['raw_data'],
		}
		]
	};
	var canvasId = '';
	var tabId = '';
	switch(metric){
		//TODO: Changes cases to actual metric labels
		case 'speed':
			canvasId = "#speedChart";
			tabId = "#speedTab";
			break;
		case 'met1':
			canvasId = "#distanceChart";
			tabId = "#distanceTab";
			break;
		case 'met2':
			canvasId = "#caloriesChart";
			tabId = "#caloriesTab";
			break;
		default:
			canvasId = "#speedChart";
			tabId = "#speedTab";
	}
	var el = '<canvas id='.concat(canvasId.substring(1),'></canvas>');

	$(canvasId).remove(); // this is my <canvas> element
	$(tabId).append(el);
	var ctx = $(canvasId).get(0).getContext("2d");
	//var ctx = document.getElementById("myChart").get(0).getContext("2d");
	new Chart(ctx, {
		type: "line",
	    	data: data_var,
	});
}
