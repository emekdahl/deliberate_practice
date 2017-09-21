var nums = [1,2,3,4];

var evens = nums.filter(function(num) {
  if (num % 2 === 0) {
    return num;
  }
});

console.log(evens); 