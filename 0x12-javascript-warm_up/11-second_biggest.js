#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const s = process.argv.length;
  const nums = [];
  for (let i = 2; i < s; i++) {
    nums[i - 2] = parseInt(process.argv[i]);
  }
  nums.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
