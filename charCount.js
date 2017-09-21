function count (string) {  
  // declare an empty obj
  var res = {};
  
  for (var i = 0; i < string.length; i++) {
   var currentChar = string[i];
   if (typeof res[currentChar] === 'undefined'){
      res[currentChar] =1;
    } else {
      res[currentChar] +=1;
    }
  } return res;
}