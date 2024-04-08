#!/usr/bin/node

const myVar = "C is fun";
const no = parseInt(process.argv[2]);
if (process.argv.length === 2) {
    console.log('Missing number of occurrences');
} else if (no) {
    for (let i=1; i <= no; i++) {
        console.log(myVar);
    }
}
