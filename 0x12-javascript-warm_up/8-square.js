#!/usr/bin/node

const myVar = 'X';

if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const no = parseInt(process.argv[2]);
  for (let i = 1; i <= no; i++) {
    console.log(myVar.repeat(no));
  }
}
