#!/usr/bin/node
exports.esrever = function (list) {
<<<<<<< HEAD
	let arr = [];
	if (list) {
		for (let i = list.length - 1; i >= 0; i--) {
			arr.push(list[i]);
		}
	}
	return arr;
}
=======
  const arr = [];
  if (list) {
    for (let i = list.length - 1; i >= 0; i--) {
      arr.push(list[i]);
    }
  }
  return arr;
};
>>>>>>> 1904012b6d7504d62dc35898f244afdb335232bf
