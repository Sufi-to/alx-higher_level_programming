#!/usr/bin/node

const myVar = "X";
const no = parseInt(process.argv[2]);
if (process.argv.length === 2) {
	console.log("Missing size");
} else if (no) {
	for (let i=1; i <= no; i++){
		console.log(myVar.repeat(no));
	}
}
