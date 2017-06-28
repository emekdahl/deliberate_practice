function mutation(str1, str2) {
  var arr1 = Array.from(str1);
  var arr2 = Array.from(str2);

  var filtered = arr1.filter(function(e){return this.indexOf(e)<0;},arr2)
  return filtered

}


console.log(mutation("burly", "ruby")); 
