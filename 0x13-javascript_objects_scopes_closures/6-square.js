#!/usr/bin/node
class Square extends Square {
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
