var product = [1,2,3].reduce(function(product,value){
  return product * value;
}, 1);

console.log(product);