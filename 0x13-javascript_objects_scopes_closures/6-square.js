#!/usr/bin/node
const Squaref = require('./5-square');

class Square extends Squaref {
    charPrint(c) {
        let char;
        if (c === undefined) {
            char = 'X';
        } else {
            char = c;
        }
        for (let i = 0; i < this.height; i++) {
            console.log(char.repeat(this.width));
        }
    }
}

module.exports = Rectangle;
