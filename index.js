var PythonShell = require('python-shell');

var myVar = setInterval(function(){ 
	startColor({ 
		x: random(0, 7),
		y: random(0, 7),
		r: random(0, 255),
		g: random(0, 255),
		b: random(0, 255)
	});
}, 100);

function random(min, max) {
	return Math.floor(Math.random() * max) + min;  
}


function startColor(color) {
	var pyshell = new PythonShell('SenseHat.py');

	console.log(color);
	pyshell.send( JSON.stringify(color) );

	pyshell.on('message', function (message) {
	  	// received a message sent from the Python script (a simple "print" statement)
		console.log("--python--");
	  	console.log(message);
	});


	pyshell.end(function (err,code,signal) {
		if (err) throw err;
		//console.log('The exit code was: ' + code);
		//console.log('The exit signal was: ' + signal);
		console.log('finished');
	});
}