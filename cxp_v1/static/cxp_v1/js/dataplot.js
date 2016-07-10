function makeplot(filepath, key1, key2) {
	console.log('../api/'.concat(filepath));
	Plotly.d3.csv('../api/'.concat(filepath), function(data) {
		processData(data, key1, key2);
	});
};

function processData(allRows, key1, key2) {
	console.log(allRows);
	var x = [], y = [];
	
	for(var i = 0; i < allRows.length; i++) {
		row = allRows[i];
		if(key1 === 0){
			x.push(i+1);
		} else {
			x.push(row[key1]);
		}
		y.push(row[key2]);
	}

	makePlotly(x,y);
};

function makePlotly(x,y) {
	var plotDiv = document.getElementById("plot");
	var traces = [{
		x: x,
		y: y
	}];
	
	Plotly.newPlot('graph1', traces, {
		title: 'Plotting local file'
	});
};
